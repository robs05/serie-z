# Generated by Django 5.1.3 on 2024-12-18 11:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serie_zeta', '0007_match_referee_alter_match_away_team_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='teams',
            field=models.ManyToManyField(blank=True, through='serie_zeta.TournamentParticipation', to='serie_zeta.team'),
        ),
    ]
