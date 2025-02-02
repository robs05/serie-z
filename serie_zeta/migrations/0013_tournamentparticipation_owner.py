# Generated by Django 5.1.3 on 2025-01-20 08:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serie_zeta', '0012_player_owner_team_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentparticipation',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tournament_participations', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
