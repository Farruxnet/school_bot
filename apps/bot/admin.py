from django.contrib import admin
from bot.models import Messages, Settings, Register


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'name', 'sex', 'username', 'address', 'phone', 'created_at']
    fields = ['user', 'course', 'username', 'name', 'sex', 'address', 'phone', 'created_at']
    list_filter = ['course', 'sex']
    readonly_fields = ['user', 'course', 'name', 'sex', 'username', 'address', 'phone', 'created_at']

    def has_add_permission(self, request):
        return False


@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['id', 'admin']

    def has_add_permission(self, request):
        if Settings.objects.all().count() >= 4:
            return False
        return True


@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    fields = ['user', 'message', 'answer', 'create_at']
    list_display = ['id', 'user', 'message', 'answer', 'create_at', 'is_answer']
    readonly_fields = ['message', 'create_at']
    list_filter = ['is_answer', ]

    def has_view_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False
