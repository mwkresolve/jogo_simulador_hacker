from django.db import models
from core.models import Jogador


class Hardware(models.Model):
    user = models.OneToOneField(Jogador, on_delete=models.CASCADE)
    cpu = models.FloatField(default=500)
    hdd = models.FloatField(default=100)
    ram = models.FloatField(default=256)
    net = models.FloatField(default=1)


