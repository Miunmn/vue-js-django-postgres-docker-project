# Generated by Django 4.0.3 on 2022-04-05 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_passengers_assigned_journey_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passengers',
            name='assigned_journey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.journeys'),
        ),
    ]
