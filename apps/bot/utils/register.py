from bot.utils.buttons import home_btn
from users.models import User
from bot.utils.language import LAN
from bot.utils.step import STEP

def user_name(message, bot):
    bot.send_message(message.chat.id, LAN['name'], parse_mode='html', reply_markup=home_btn())
    User.objects.filter(tg_id=message.chat.id).update(step=STEP['DEFAULT'])

def user_sex(message, bot):
    pass

def user_address(message, bot):
    pass

def user_phone_number(message, bot):
    pass