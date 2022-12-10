import traceback

from django.shortcuts import HttpResponse
import telebot
from django.conf import settings
import json

from telebot import types

from bot.models import Register
from bot.utils.contact_message import contact_message
from bot.utils.buttons import start_button, courses_button, home_btn
from bot.utils.helpers import entry_language, get_user_lan
from bot.utils.language import LAN
from bot.utils.register import course_detail, user_name, user_sex, user_address, user_phone_number
from bot.utils.step import STEP
from users.models import User
from data.models import StartText, About, ContactInfo, Faq, Courses

bot = telebot.TeleBot(settings.TOKEN)


def web_hook(request):
    if request.method == "POST":
        try:
            try:
                if 'my_chat_member' in json.loads(request.body.decode('utf-8')).keys():
                    if json.loads(request.body.decode('utf-8'))['my_chat_member']['new_chat_member'][
                        'status'] == 'kicked':
                        User.objects.filter(
                            tg_id=json.loads(request.body.decode('utf-8'))['my_chat_member']['chat']['id']).update(
                            status='0')
                    elif json.loads(request.body.decode('utf-8'))['my_chat_member']['new_chat_member'][
                        'status'] == 'member':
                        data = json.loads(request.body.decode('utf-8'))['my_chat_member']
                        if 'last_name' in json.loads(request.body.decode('utf-8')).keys():
                            name = data['chat']['first_name'] + ' ' + data['chat']['last_name']
                        else:
                            name = data['chat']['first_name']
                        User.objects.filter(
                            tg_id=json.loads(request.body.decode('utf-8'))['my_chat_member']['chat']['id']
                        ).update(
                            status='2',
                            name=name,
                            username=data['chat']['username']
                        )
            except Exception as e:
                pass

            bot.process_new_updates([telebot.types.Update.de_json(request.body.decode('utf-8'))])
        except Exception as e:
            print(e)

        return HttpResponse(status=200)
    s = '<a href="https://api.telegram.org/bot{0}/setWebhook?url={1}/bot-hook/">WEB</a>'.format(settings.TOKEN,
                                                                                                settings.WEBHOOK)
    return HttpResponse(s)


@bot.message_handler(commands=['start'])
def start(message):
    if User.objects.filter(tg_id=message.chat.id).exists() is False:
        if message.chat.last_name:
            name = message.chat.first_name + ' ' + message.chat.last_name
        else:
            name = message.chat.first_name
        User.objects.create(
            tg_id=message.chat.id,
            name=name,
            language='oz',
            username=message.from_user.username,
            step=STEP['DEFAULT'],
        )
        lan_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
        lan_button.add(*[LAN['oz_text'], LAN['ru_text']])
        bot.send_message(message.chat.id, LAN['choose_lan'], parse_mode='html', reply_markup=lan_button)
        User.objects.filter(tg_id=message.chat.id).update(step=STEP['LAN'])
        return
    lan = User.objects.get(tg_id=message.chat.id).language
    text = StartText.objects.last().text if lan == 'oz' else StartText.objects.last().text_ru
    try:
        bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=start_button(message.chat.id))
    except Exception as e:
        print(traceback.format_exc())
        print(e)


@bot.message_handler(func=lambda msg: msg.text == LAN[get_user_lan(msg.chat.id)]['home'])
def home(message):
    try:
        start(message)
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda msg: msg.text == LAN[get_user_lan(msg.chat.id)]['courses'])
def courses(message):
    lan = User.objects.get(tg_id=message.chat.id).language
    bot.send_message(message.chat.id, LAN[lan]['courses'], parse_mode='html', reply_markup=courses_button(lan))
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSES'])


@bot.message_handler(func=lambda msg: msg.text == LAN[get_user_lan(msg.chat.id)]['contact_us'])
def courses(message):
    try:
        bot.send_message(message.chat.id, ContactInfo.objects.last().contact, parse_mode='html',
                         reply_markup=home_btn(message.chat.id))
    except Exception as e:
        print(e)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['CONTACT_US'])


@bot.message_handler(func=lambda msg: msg.text == LAN[get_user_lan(msg.chat.id)]['change_lan'])
def change_lan(message):
    lan_button = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    lan_button.add(*[LAN['oz_text'], LAN['ru_text']])
    bot.send_message(message.chat.id, LAN['choose_lan'], parse_mode='html', reply_markup=lan_button)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['LAN'])


@bot.message_handler(func=lambda msg: msg.text == LAN[get_user_lan(msg.chat.id)]['faq'])
def faq(message):
    lan = User.objects.get(tg_id=message.chat.id).language
    faq = Faq.objects.last().faq if lan == 'oz' else Faq.objects.last().faq_ru
    bot.send_message(message.chat.id, faq, parse_mode='html', reply_markup=home_btn(message.chat.id))


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    user_id = call.message.chat.id
    lan = get_user_lan(user_id)
    if Register.objects.filter(user__tg_id=user_id, status=False).exists():
        Register.objects.filter(user__tg_id=user_id, status=False).delete()
    Register.objects.create(
        user=User.objects.get(tg_id=user_id),
        course=Courses.objects.get(id=call.data.split('_')[1])
    )
    bot.send_message(user_id, LAN[lan]['name'], parse_mode='html', reply_markup=home_btn(user_id))
    User.objects.filter(tg_id=user_id).update(step=STEP['COURSE_REGISTER'])


@bot.message_handler(func=lambda msg: msg.text == LAN[get_user_lan(msg.chat.id)]['about'])
def courses(message):
    photo = About.objects.last()
    lan = User.objects.get(tg_id=message.chat.id).language
    text = About.objects.last().text if lan == 'oz' else About.objects.last().text_ru
    try:
        photo_id = open(f'{settings.BASE_DIR}/media/{photo.image}', 'rb')
        bot.send_photo(
            message.chat.id,
            photo_id,
            text,
            parse_mode='html',
        )
    except Exception as e:
        print(traceback.print_exc())
        print(e)


@bot.message_handler(content_types=['text', 'contact'])
def text(message):
    try:
        user_step = User.objects.get(tg_id=message.chat.id).step
        switcher = {
            STEP['DEFAULT']: home,
            STEP['CONTACT_US']: contact_message,
            STEP['COURSES']: course_detail,
            STEP['COURSE_REGISTER']: user_name,
            STEP['COURSE_SEX']: user_sex,
            STEP['COURSE_ADDRESS']: user_address,
            STEP['COURSE_PHONE']: user_phone_number,
            STEP['LAN']: entry_language,
        }
        func = switcher.get(user_step, lambda: home(message))
        func(message, bot)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
