from django.conf import settings
from telebot import types

from bot.models import Register
from bot.utils.buttons import home_btn, bottom_button, start_button
from data.models import Courses
from users.models import User
from bot.utils.language import LAN
from bot.utils.step import STEP


def course_detail(message, bot):
    try:
        course = Courses.objects.get(name=message.text)
        course_register_button = types.InlineKeyboardMarkup(row_width=1)
        course_register_button.add(types.InlineKeyboardButton(text=LAN['register'], callback_data=f'reg_{course.id}'))
        photo_id = open(f'{settings.BASE_DIR}/media/{course.image}', 'rb')
        text = f"<b>{course.name}</b>\n\n{course.description}"
        bot.send_photo(
            message.chat.id,
            photo_id,
            text,
            parse_mode='html',
            reply_markup=course_register_button
        )
    except Exception as e:
        print(e)
        bot.send_message(message.chat.id, LAN['error'], parse_mode='html')


def user_name(message, bot):
    Register.objects.filter(
        user__tg_id=message.chat.id,
        status=False
    ).update(
        name=message.text,
        username=message.from_user.username
    )
    sex_btn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    sex_btn.add(*[LAN['man'], LAN['woman']])
    sex_btn.add(*bottom_button())
    bot.send_message(message.chat.id, LAN['sex'], parse_mode='html', reply_markup=sex_btn)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSE_SEX'])


def user_sex(message, bot):
    if message.text == LAN['man']:
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
    address_btn.add(*bottom_button())
    bot.send_message(message.chat.id, LAN['address'], parse_mode='html', reply_markup=address_btn)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSE_ADDRESS'])


def user_address(message, bot):
    Register.objects.filter(
        user__tg_id=message.chat.id,
        status=False
    ).update(
        address=message.text
    )
    phone_btn = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    phone_btn.add(types.KeyboardButton(text=LAN['phone_number_btn'], request_contact=True))
    phone_btn.add(*bottom_button())
    bot.send_message(message.chat.id, LAN['phone_number'], parse_mode='html', reply_markup=phone_btn)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSE_PHONE'])


def user_phone_number(message, bot):
    try:
        phone_number = message.contact.phone_number
    except Exception as e:
        phone_number = message.text
    Register.objects.filter(
        user__tg_id=message.chat.id,
        status=False
    ).update(
        phone=phone_number,
        status=True
    )
    bot.send_message(message.chat.id, LAN['success_register'], parse_mode='html', reply_markup=start_button())
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['DEFAULT'])
