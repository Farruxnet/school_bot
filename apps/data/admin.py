from django.contrib import admin
from data.models import Faq, Courses, CoursesDescription, ContactInfo, StartText, About

admin.site.site_header = 'Boshqaruv paneli'
admin.site.site_title = 'Boshqaruv paneli'
admin.site.index_title = ""

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if Faq.objects.all():
            return False
        return True

admin.site.register(Courses)
admin.site.register(CoursesDescription)
admin.site.register(ContactInfo)
admin.site.register(StartText)
admin.site.register(About)