# Generated by Django 5.1.3 on 2024-11-26 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serie_zeta', '0004_tournament_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referee',
            name='exeperience',
            field=models.IntegerField(null=True),
        ),
    ]