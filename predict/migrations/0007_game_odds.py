# Generated by Django 4.1.3 on 2022-12-12 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0006_game_season'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='odds',
            field=models.FloatField(null=True),
        ),
    ]
