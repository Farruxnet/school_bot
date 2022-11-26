from django.contrib import admin
from bot.models import Messages, Settings

@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'admin']
    
    def has_add_permission(self, request):
        if Settings.objects.all():
            return False
        return True
@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    fields = ['user', 'message', 'answer', 'create_at']
    list_display = ['id', 'user', 'message', 'answer', 'create_at']
    readonly_fields = ['message', 'create_at']

    def has_add_permission(self, request):
        return False