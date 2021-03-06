# Generated by Django 4.0.3 on 2022-04-11 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_drivers_has_assigned_bus'),
    ]

    operations = [
        migrations.AddField(
            model_name='buses',
            name='has_assigned_journey',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='buses',
            name='driver',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.drivers'),
        ),
        migrations.RemoveField(
            model_name='journeys',
            name='buses',
        ),
        migrations.AddField(
            model_name='journeys',
            name='buses',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='backend.buses'),
        ),
    ]
