# Generated by Django 4.1.3 on 2022-12-08 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rtg_history',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rtg', models.FloatField()),
                ('date', models.DateField()),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='predict.team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('home_score', models.IntegerField(null=True)),
                ('away_score', models.IntegerField(null=True)),
                ('away_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='predict.team')),
                ('home_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='predict.team')),
                ('predicted_winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='predicted_winner', to='predict.team')),
                ('winner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='predict.team')),
            ],
        ),
    ]
