from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import telebot
bot = telebot.TeleBot(settings.TOKEN)
from bot.models import Messages

@receiver(post_save, sender=Messages)
def answer(sender, instance, created, **kwargs):
    if not created:
        bot.send_message(
            instance.user.tg_id,
            instance.answer,
            parse_mode='html'
        )
        Messages.objects.filter(id=instance.id).update(is_answer=True)