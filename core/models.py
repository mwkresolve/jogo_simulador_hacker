from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import generate_unique_ip, generate_random_password
from django.db.models.signals import post_save
from django.dispatch import receiver

class Jogador(AbstractUser):
    ip_address = models.CharField(max_length=15, unique=True, default=generate_unique_ip)
    game_pass = models.CharField(max_length=8, default=generate_random_password())
    log = models.TextField(default='')
    is_bot = models.BooleanField(default=False)

    def __str__(self):
        return self.username


@receiver(post_save, sender='core.Jogador')
def create_hardware(sender, instance, created, **kwargs):
    if created:
        from hardware.models import Hardware
        Hardware.objects.create(user=instance)
