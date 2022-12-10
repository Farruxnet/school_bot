from django.contrib import admin
from data.models import Faq, Courses, CoursesDescription, ContactInfo, StartText, About, Language, Messages
from django_json_widget.widgets import JSONEditorWidget
from django.db.models import JSONField

admin.site.site_header = 'Boshqaruv paneli'
admin.site.site_title = 'Boshqaruv paneli'
admin.site.index_title = ""

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('oz', 'date', 'count', 'not_send_count', 'status')
    exclude = ('image_id', 'status', 'count', 'not_send_count', 'date',)

    def has_add_permission(self, request, obj=None):
        if Messages.objects.filter(status=False).exists():
            return False
        else:
            return True

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Faq.objects.all():
            return False
        return True
class LanguageDataAdmin(admin.ModelAdmin):

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        if Language.objects.all():
            return False
        else:
            return True
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }

admin.site.register(Language, LanguageDataAdmin)
admin.site.register(Courses)
# admin.site.register(CoursesDescription)
admin.site.register(ContactInfo)
admin.site.register(StartText)
admin.site.register(About)