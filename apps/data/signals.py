import threading
from time import time

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import telebot
import os

from bot.models import Settings
from data.models import Language, Messages
from users.models import User

bot = telebot.TeleBot(settings.TOKEN)


@receiver(post_save, sender=Language)
def reboot_gunicorn(sender, instance, created, **kwargs):
    if created:
        print('create')
    else:
        print(45)
        if not settings.DEBUG:
            print(12)
            os.system("systemctl restart school")


@receiver(post_save, sender=Messages)
def messages(sender, instance, created, **kwargs):
    if created:
        try:
            admins = Settings.objects.all().last()
            try:
                admin_id = admins.admin.tg_id
            except:
                admin_id = 313578337

            path_photo = str(settings.BASE_DIR) + "/media/" + str(Messages.objects.get(status=False).image)
            URL = 'https://api.telegram.org/bot' + settings.TOKEN + '/sendPhoto'
            with open(path_photo, 'rb') as f:
                file = {'photo': f}
                data = {'chat_id': admin_id}
                r = requests.post(URL, files=file, data=data)
                Messages.objects.filter(status=False).update(image_id=r.json()['result']['photo'][0]['file_id'])

            for usermessage in Messages.objects.filter(status=False):
                id = usermessage.id
                text_oz = usermessage.oz
                text_ru = usermessage.ru
                message_status = usermessage.status
                image_id = usermessage.image_id
        except Exception as e:
            bot.send_message(313578337, f'{str(e)}')

        def forever():
            if message_status is False:
                try:
                    ok_send = 0
                    no_send = 0
                    user_1 = User.objects.all()
                    for send in user_1:
                        try:
                            if send.language == "oz":
                                bot.send_photo(send.tg_id, image_id, text_oz, parse_mode='HTML')
                            elif send.language == "ru":
                                bot.send_photo(send.tg_id, image_id, text_ru, parse_mode='HTML')
                            ok_send += 1
                            time.sleep(0.2)
                        except Exception as e:
                            no_send += 1
                    Messages.objects.filter(status=False, id=id).update(status=True, count=ok_send,
                                                                        not_send_count=no_send)
                except Exception as e:
                    print(e)
            else:
                print(123)
        t1 = threading.Thread(target=forever)
        t1.start()

    else:
        print('update')
