# Generated by Django 4.2.2 on 2023-06-07 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_jogador_game_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='game_pass',
            field=models.CharField(default='3TgwTPEY', max_length=8),
        ),
    ]