from telebot import types
import telebot
from django.conf import settings
from data.models import Courses
bot = telebot.TeleBot(settings.TOKEN)
from bot.utils.language import LAN

def home_button():
    return [LAN['courses'], LAN['about'], LAN['contact_us']]

def bottom_button():
    return [LAN['home']]

def home_btn():
    home_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    home_button.add(*bottom_button())
    return home_button

def start_button():
    start_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    start_button.add(*home_button())
    start_button.add(*[LAN['faq']])
    return start_button

def courses_button():
    courses_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    courses_button.add(*[course.name for course in Courses.objects.all()])
    courses_button.add(*bottom_button())
    return courses_button