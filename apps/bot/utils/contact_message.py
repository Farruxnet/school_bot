from bot.utils.buttons import start_button
from bot.utils.language import LAN
from bot.utils.step import STEP
from django.conf import settings
from users.models import User
from bot.models import Messages, Settings

def contact_message(message, bot):
    admins = Settings.objects.all()
    user = User.objects.get(tg_id=message.chat.id)
    message_id = Messages.objects.create(
        user=user,
        message_id=message.message_id,
        message=message.text
    ).id
    try:
        text = f"<b>{LAN['new_message']}</b>\n\n{message.text}\n\n<a href='{settings.HOST}/admin/bot/messages/{message_id}/change/'>{LAN['answer']}</a>"
        for admin in admins:
            bot.send_message(
                admin.admin.tg_id,
                text,
                parse_mode='html'
            )
        bot.send_message(message.chat.id, LAN['success_message'], parse_mode='html', reply_markup=start_button())
        User.objects.filter(tg_id=message.chat.id).update(step=STEP['DEFAULT'])
    except Exception as e:
        print(e)
