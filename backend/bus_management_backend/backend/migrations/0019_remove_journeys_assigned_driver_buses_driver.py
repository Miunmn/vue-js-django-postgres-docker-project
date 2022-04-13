# Generated by Django 4.0.3 on 2022-04-11 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_remove_journeys_assigned_bus_journeys_buses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journeys',
            name='assigned_driver',
        ),
        migrations.AddField(
            model_name='buses',
            name='driver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.drivers'),
        ),
    ]