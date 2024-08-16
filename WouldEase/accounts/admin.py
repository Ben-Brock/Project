from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Region, Country, CustomUser
# Register your models here.
admin.site.register(Region)
admin.site.register(Country)
admin.site.register(CustomUser, UserAdmin)

