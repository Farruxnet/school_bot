from django.urls import path
from bot.views.hook import web_hook
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', csrf_exempt(web_hook))
]