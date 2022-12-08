from telebot import types
import telebot
from django.conf import settings

from data.models import Courses
from users.models import User

bot = telebot.TeleBot(settings.TOKEN)
from bot.utils.language import LAN

def home_button(lan):
    return [LAN[lan]['courses'], LAN[lan]['about'], LAN[lan]['contact_us']]

def bottom_button(lan):
    return [LAN[lan]['home']]

def home_btn(tg_id):
    lan = User.objects.get(tg_id=tg_id).language
    home_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    home_button.add(*bottom_button(lan))
    return home_button

def start_button(tg_id):
    lan = User.objects.get(tg_id=tg_id).language
    start_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    start_button.add(*home_button(lan))
    start_button.add(*[LAN[lan]['faq']])
    return start_button

def courses_button(lan):
    courses_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    courses_button.add(*[course.name for course in Courses.objects.all()])
    courses_button.add(*bottom_button(lan))
    return courses_button