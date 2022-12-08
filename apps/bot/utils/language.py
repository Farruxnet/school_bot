from data.models import Language
try:
    lan = Language.objects.last()
except:
    lan = ""

try:
    LAN = {
        "choose_lan": "Tilni tanlang",
        "oz_text": "O'zbek",
        "ru_text": "Руский",
        "oz": lan.oz,
        "ru": lan.ru
    }
except:
    pass