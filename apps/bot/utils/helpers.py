from django.conf import settings
from telebot import types

from bot.models import Register
from bot.utils.buttons import start_button
from data.models import Courses, StartText
from users.models import User
from bot.utils.language import LAN
from bot.utils.step import STEP


def get_user_lan(user_id):
    try:
        return User.objects.get(tg_id=user_id).language
    except:
        pass


def entry_language(message, bot):
    lan = 'oz'
    if message.text == LAN['ru_text']:
        lan = 'ru'
    User.objects.filter(tg_id=message.chat.id).update(language=lan, step=STEP['DEFAULT'])
    lan = User.objects.get(tg_id=message.chat.id).language
    text = StartText.objects.last().text if lan == 'oz' else StartText.objects.last().text_ru
    bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=start_button(message.chat.id))
