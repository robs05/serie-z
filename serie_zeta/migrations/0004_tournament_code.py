# Generated by Django 5.1.3 on 2024-11-25 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serie_zeta', '0003_alter_tournamentparticipation_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='code',
            field=models.CharField(default=datetime.datetime(2024, 11, 25, 8, 43, 25, 217139, tzinfo=datetime.timezone.utc), max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
