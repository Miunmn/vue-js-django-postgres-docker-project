# Generated by Django 4.0.3 on 2022-04-12 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0029_remove_buses_has_assigned_journey_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='passengers',
            old_name='assigned_journey',
            new_name='journey',
        ),
        migrations.AddField(
            model_name='passengers',
            name='bus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='backend.buses'),
        ),
    ]
