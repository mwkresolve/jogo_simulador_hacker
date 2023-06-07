from django.contrib import admin
from .models import Jogador

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('username', 'ip_address', 'game_pass')
