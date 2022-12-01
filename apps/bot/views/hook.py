from django.shortcuts import HttpResponse
import telebot
from django.conf import settings
import json

from bot.utils.contact_message import contact_message
from bot.utils.buttons import start_button, courses_button, home_btn
from bot.utils.language import LAN
from bot.utils.register import course_detail, user_name, user_sex, user_address, user_phone_number
from bot.utils.step import STEP
from users.models import User
from data.models import StartText, About, ContactInfo, Faq

bot = telebot.TeleBot(settings.TOKEN)

def web_hook(request):
    if request.method == "POST":
        try:
            try:
                if 'my_chat_member' in json.loads(request.body.decode('utf-8')).keys():
                    if json.loads(request.body.decode('utf-8'))['my_chat_member']['new_chat_member']['status'] == 'kicked':
                        User.objects.filter(tg_id = json.loads(request.body.decode('utf-8'))['my_chat_member']['chat']['id']).update(status = '0')
                    elif json.loads(request.body.decode('utf-8'))['my_chat_member']['new_chat_member']['status'] == 'member':
                        data = json.loads(request.body.decode('utf-8'))['my_chat_member']
                        if 'last_name' in json.loads(request.body.decode('utf-8')).keys():
                            name = data['chat']['first_name'] + ' ' + data['chat']['last_name']
                        else:
                            name = data['chat']['first_name']
                        User.objects.filter(
                            tg_id = json.loads(request.body.decode('utf-8'))['my_chat_member']['chat']['id']
                        ).update(
                            status = '2',
                            name = name,
                            username = data['chat']['username']
                        )
            except Exception as e:
                pass

            bot.process_new_updates([telebot.types.Update.de_json(request.body.decode('utf-8'))])
        except Exception as e:
            print(e)


        return HttpResponse(status=200)
    s = '<a href="https://api.telegram.org/bot{0}/setWebhook?url={1}/bot-hook/">WEB</a>'.format(settings.TOKEN, settings.WEBHOOK)
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
    bot.send_message(message.chat.id, StartText.objects.last().text, parse_mode='html', reply_markup=start_button())
@bot.message_handler(func=lambda msg: msg.text==LAN['home'])
def home(message):
    try:
        start(message)
    except Exception as e:
        print(e)
@bot.message_handler(func=lambda msg: msg.text == LAN['courses'])
def courses(message):
    bot.send_message(message.chat.id, LAN['courses'], parse_mode='html', reply_markup=courses_button())
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['COURSES'])

@bot.message_handler(func=lambda msg: msg.text == LAN['contact_us'])
def courses(message):
    try:
        bot.send_message(message.chat.id, ContactInfo.objects.last().contact, parse_mode='html', reply_markup=home_btn())
    except Exception as e:
        print(e)
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['CONTACT_US'])

@bot.message_handler(func=lambda msg: msg.text == LAN['faq'])
def faq(message):
    bot.send_message(message.chat.id, Faq.objects.last().faq, parse_mode='html', reply_markup=courses_button())


@bot.callback_query_handler(func=lambda call: True)
def call_back(call):
    user_id = call.message.chat.id
    bot.send_message(user_id, LAN['name'], parse_mode='html', reply_markup=home_btn())
    User.objects.filter(tg_id=user_id).update(step=STEP['COURSE_REGISTER'])


@bot.message_handler(func=lambda msg: msg.text == LAN['about'])
def courses(message):
    text = About.objects.last().text
    photo = About.objects.last()
    try:
        photo_id = open(f'{settings.BASE_DIR}/media/{photo.image}', 'rb')
        bot.send_photo(
            message.chat.id,
            photo_id,
            text,
            parse_mode='html',
        )
    except Exception as e:
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
            STEP['COURSE_NAME']: user_sex,
            STEP['COURSE_ADDRESS']: user_address,
            STEP['COURSE_PHONE']: user_phone_number,
        }
        func = switcher.get(user_step, lambda: home(message))
        func(message, bot)
    except Exception as e:
        print(e)
