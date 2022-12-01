from django.shortcuts import render
from django.conf import settings

def index(request):
    print(settings.STATICFILES_DIR)
    print(settings.BASE_DIR)
    return render(request, 'index.html')
