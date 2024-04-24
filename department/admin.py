from django.contrib import admin
from .models import *

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
admin.site.register(CustomUser, CustomUserAdmin)
# Register your models here.

class CustomTokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'user']
admin.site.register(CustomToken, CustomTokenAdmin)
