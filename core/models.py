from django.contrib.auth.models import AbstractUser
from django.db import models
from .utils import *


class Jogador(AbstractUser):
    ip_address = models.CharField(max_length=15, unique=True, default=generate_unique_ip)


    def __str__(self):
        return self.username
