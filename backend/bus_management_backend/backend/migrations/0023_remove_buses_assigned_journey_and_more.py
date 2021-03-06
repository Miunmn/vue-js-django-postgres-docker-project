# Generated by Django 4.0.3 on 2022-04-11 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0022_remove_buses_has_assigned_journey_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buses',
            name='assigned_journey',
        ),
        migrations.AddField(
            model_name='buses',
            name='has_assigned_journey',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='journeys',
            name='buses',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.buses'),
        ),
    ]
