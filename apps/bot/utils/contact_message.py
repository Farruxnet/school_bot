from bot.utils.buttons import start_button
from bot.utils.language import LAN
from bot.utils.step import STEP
from users.models import User
from bot.models import Messages, Settings

def contact_message(message, bot):
    admin = Settings.objects.last().admin.tg_id
    user = User.objects.get(tg_id=message.chat.id)
    Messages.objects.create(
        user=user,
        message_id=message.message_id,
        message=message.text
    )
    try:
        bot.forward_message(admin, message.chat.id, message.message_id)
        bot.send_message(message.chat.id, LAN['success_message'], parse_mode='html', reply_markup=start_button())
        User.objects.filter(tg_id=message.chat.id).update(step=STEP['DEFAULT'])
    except Exception as e:
        print(e)
