from django.contrib import admin
from django.contrib.auth.models import Group
from . models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django import forms

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('phone_number', 'password',  'is_active', 'is_admin')


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    date_hierarchy = 'create_at'
    exclude = ('status_check',)
    search_fields = ['phone_number', 'name', 'username']
    list_display = ('name', 'status', 'create_at')
    list_filter = ('is_admin', 'status', 'language')
    fieldsets = (
        (None, {'fields': ('phone_number', 'name', 'language', 'status', 'username', 'description', 'amount', 'tg_id', 'step',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ( 'tg_id', 'phone_number', 'password1', 'password2', 'name', 'language', 'status', 'description', 'amount',),
        }),
    )
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
