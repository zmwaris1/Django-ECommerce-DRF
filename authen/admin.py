from django.contrib import admin
from .models import User
from django.contrib.auth import admin as ad

# Register your models here.

class UserAdmin(ad.UserAdmin):
    list_display = ('username', 'email', 'phone_number',)
admin.site.register(User, UserAdmin)
