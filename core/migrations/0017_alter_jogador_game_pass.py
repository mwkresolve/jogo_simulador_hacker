# Generated by Django 4.2.2 on 2023-06-08 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_alter_jogador_game_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='game_pass',
            field=models.CharField(default='napzCYbE', max_length=8),
        ),
    ]