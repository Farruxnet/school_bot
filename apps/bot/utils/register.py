from django.conf import settings
from telebot import types

from bot.utils.buttons import home_btn
from data.models import Courses
from users.models import User
from bot.utils.language import LAN
from bot.utils.step import STEP

def course_detail(message, bot):
    try:
        course = Courses.objects.get(name = message.text)
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
    bot.send_message(message.chat.id, LAN['name'], parse_mode='html', reply_markup=home_btn())
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSE_REGISTER'])

def user_sex(message, bot):
    pass

def user_address(message, bot):
    pass

def user_phone_number(message, bot):
    pass