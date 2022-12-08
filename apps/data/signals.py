from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import telebot
import os
from data.models import Language

bot = telebot.TeleBot(settings.TOKEN)


@receiver(post_save, sender=Language)
def reboot_gunicorn(sender, instance, created, **kwargs):
    if created:
        print('create')
    else:
        print(45)
        if not settings.DEBUG:
            print(12)
            os.system("sudo systemctl restart school")