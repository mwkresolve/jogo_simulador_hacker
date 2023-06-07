from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Jogador
from hardware.models import Hardware

@receiver(post_save, sender=Jogador)
def create_hardware(sender, instance, created, **kwargs):
    if created:
        Hardware.objects.create(user=instance)
