# Generated by Django 4.2.2 on 2023-06-07 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_jogador_is_bot_alter_jogador_game_pass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogador',
            name='game_pass',
            field=models.CharField(default='sGhtagzv', max_length=8),
        ),
    ]