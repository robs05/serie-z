# Generated by Django 5.1.3 on 2024-12-02 09:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serie_zeta', '0006_alter_player_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='referee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='serie_zeta.referee'),
        ),
        migrations.AlterField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='away_team_match', to='serie_zeta.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='home_team_match', to='serie_zeta.team'),
        ),
    ]