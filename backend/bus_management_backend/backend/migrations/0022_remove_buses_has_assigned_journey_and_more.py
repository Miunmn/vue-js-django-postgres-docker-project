# Generated by Django 4.0.3 on 2022-04-11 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0021_buses_has_assigned_journey_alter_buses_driver_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buses',
            name='has_assigned_journey',
        ),
        migrations.RemoveField(
            model_name='journeys',
            name='buses',
        ),
        migrations.AddField(
            model_name='buses',
            name='assigned_journey',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.journeys'),
        ),
    ]
