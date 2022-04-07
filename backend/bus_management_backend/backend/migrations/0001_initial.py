# Generated by Django 4.0.3 on 2022-04-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buses',
            fields=[
                ('bus_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('plate', models.CharField(max_length=7)),
                ('years_of_service', models.IntegerField()),
            ],
            options={
                'db_table': 'buses',
            },
        ),
        migrations.CreateModel(
            name='Drivers',
            fields=[
                ('driver_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('age', models.IntegerField(max_length=2)),
            ],
            options={
                'db_table': 'drivers',
            },
        ),
        migrations.CreateModel(
            name='Journeys',
            fields=[
                ('journey_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('journey_name', models.CharField(max_length=10)),
                ('assigned_bus', models.IntegerField(max_length=3)),
            ],
            options={
                'db_table': 'journeys',
            },
        ),
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('passenger_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'passengers',
            },
        ),
    ]