# Generated by Django 4.0.3 on 2022-04-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_alter_buses_plate_alter_journeys_journey_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='buses',
            name='capacity',
            field=models.IntegerField(default=10),
        ),
    ]
