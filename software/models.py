from django.db import models
from core.models import Jogador

class SoftwareType(models.Model):
    type_id = models.CharField(max_length=2, primary_key=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.description


class Software(models.Model):
    user = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    type_of_software = models.ForeignKey(SoftwareType, on_delete=models.CASCADE)
    soft_name = models.CharField(max_length=25, default='soft')
    soft_version = models.IntegerField()
    soft_size = models.IntegerField()
    soft_ram = models.IntegerField()
    soft_hidden = models.BooleanField(default=0)
    soft_hidden_with = models.BigIntegerField(default=0)
    # outros campos do modelo

    def __str__(self):
        return f"Software {self.pk}"
