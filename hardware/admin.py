from django.contrib import admin
from .models import Hardware

class HardwareAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpu', 'hdd', 'ram', 'net']


admin.site.register(Hardware, HardwareAdmin)
