from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Jogador
from hardware.models import Hardware
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .utils import *


@receiver(post_save, sender=Jogador)
def create_hardware(sender, instance, created, **kwargs):
    if created:
        try:
            Hardware.objects.create(user=instance)
        except:
            pass



@receiver(post_migrate)
def create_bots(sender, **kwargs):
    if sender.name == 'core':
        if not Jogador.objects.filter(is_bot=True).exists():
            bot_names = [
                'ZeroGuy', 'BlackHatElite', 'CryptoPhantom', 'CyberNinja', 'DarkWebWarrior',
                'HackerKingpin', 'PhantomGhost', 'CrypticByte', 'StealthViper', 'CyberMatrix',
                'DarkByte', 'ShadowHacker', 'CryptoGhost', 'CyberPhantom', 'BlackHatMatrix',
                'DarkNinja', 'PhantomByte', 'StealthMatrix', 'CryptoViper', 'HackerGhost',
                'ShadowByte', 'PhantomHacker', 'DarkGhost', 'BlackHatPhantom', 'CyberViper',
                'CryptoMatrix', 'StealthGhost', 'HackerPhantom', 'ShadowViper', 'DarkHacker',
            ]

            for name in bot_names:
                if name == 'mwk':
                    Jogador.objects.create(username=name, is_bot=True, ip_address='0.0.0.0')
                Jogador.objects.create(username=name, is_bot=True)
