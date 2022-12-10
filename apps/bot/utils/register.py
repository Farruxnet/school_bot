import traceback

from django.conf import settings
from telebot import types

from bot.models import Register
from bot.utils.buttons import home_btn, bottom_button, start_button
from data.models import Courses
from users.models import User
from bot.utils.language import LAN
from bot.utils.step import STEP


def course_detail(message, bot):
    lan = User.objects.get(tg_id=message.chat.id).language
    try:
        if lan == "oz":
            course = Courses.objects.get(name=message.text)
            text = f"<b>{course.name}</b>\n\n{course.description}"
        else:
            course = Courses.objects.get(name_ru=message.text)
            text = f"<b>{course.name_ru}</b>\n\n{course.description_ru}"
        course_register_button = types.InlineKeyboardMarkup(row_width=1)
        course_register_button.add(types.InlineKeyboardButton(text=LAN[lan]['register'], callback_data=f'reg_{course.id}'))
        photo_id = open(f'{settings.BASE_DIR}/media/{course.image}', 'rb')
        bot.send_photo(
            message.chat.id,
            photo_id,
            text,
            parse_mode='html',
            reply_markup=course_register_button
        )
    except Exception as e:
        print(traceback.print_exc())
        print(e)
        bot.send_message(message.chat.id, LAN[lan]['error'], parse_mode='html')


def user_name(message, bot):
    lan = User.objects.get(tg_id=message.chat.id).language
    Register.objects.filter(
        user__tg_id=message.chat.id,
        status=False
    ).update(
        name=message.text,
        username=message.from_user.username
    )
    sex_btn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    sex_btn.add(*[LAN[lan]['man'], LAN[lan]['woman']])
    sex_btn.add(*bottom_button(lan))
    bot.send_message(message.chat.id, LAN[lan]['sex'], parse_mode='html', reply_markup=sex_btn)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSE_SEX'])


def user_sex(message, bot):
    lan = User.objects.get(tg_id=message.chat.id).language
    if message.text == LAN[lan]['man']:
        sex = 'man'
    else:
        sex = 'woman'
    Register.objects.filter(
        user__tg_id=message.chat.id,
        status=False
    ).update(
        sex=sex
    )
    address_btn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    address_btn.add(*bottom_button(lan))
    bot.send_message(message.chat.id, LAN[lan]['address'], parse_mode='html', reply_markup=address_btn)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSE_ADDRESS'])


def user_address(message, bot):
    lan = User.objects.get(tg_id=message.chat.id).language
    Register.objects.filter(
        user__tg_id=message.chat.id,
        status=False
    ).update(
        address=message.text
    )
    phone_btn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    phone_btn.add(types.KeyboardButton(text=LAN[lan]['phone_number_btn'], request_contact=True))
    phone_btn.add(*bottom_button(lan))
    bot.send_message(message.chat.id, LAN[lan]['phone_number'], parse_mode='html', reply_markup=phone_btn)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSE_PHONE'])


def user_phone_number(message, bot):
    lan = User.objects.get(tg_id=message.chat.id).language
    try:
        phone_number = message.contact.phone_number
    except Exception as e:
        phone_number = message.text
    url = Register.objects.get(user__tg_id=message.chat.id, status=False).course.telegram_group
    Register.objects.filter(
        user__tg_id=message.chat.id,
        status=False
    ).update(
        phone=phone_number,
        status=True
    )

    succsess_btn = types.InlineKeyboardMarkup(row_width=1)
    succsess_btn.add(types.InlineKeyboardButton(text=LAN[lan]['group'], url=url))
    succsess_text = LAN[lan]['success_register']
    bot.send_message(message.chat.id, succsess_text, parse_mode='html', reply_markup=succsess_btn)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['DEFAULT'])
