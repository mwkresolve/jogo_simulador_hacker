# Generated by Django 4.2.2 on 2023-06-07 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogador',
            name='game_pass',
            field=models.CharField(default='G1jtMLBA', max_length=8),
        ),
    ]
