from django.contrib import admin
from django.urls import path, include

from bot.views.views import index

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('bot-hook/', include('bot.urls')),
]
