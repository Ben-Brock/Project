from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Region, Country, CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email','age', 'is_staff']

# Register your models here.
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(CustomUser, CustomUserAdmin)

