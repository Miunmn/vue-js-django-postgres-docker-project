from django.db import models
# from django.core.validators import MinLengthValidator, MinValueValidator
import django

class Buses(models.Model):
    bus_id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=7, unique=True)
    years_of_service = models.IntegerField()
    class Meta:
        db_table = 'buses'
 


class Drivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)
    class Meta:
        db_table = 'drivers'


class Journeys(models.Model):
    journey_id = models.AutoField(primary_key=True)
    journey_name = models.CharField(max_length=10, unique=True)  
    from_city = models.CharField(max_length=50, default='' )
    to_city = models.CharField(max_length=50, default='')
    assigned_driver = models.ForeignKey(Drivers, on_delete=models.CASCADE)
    assigned_bus = models.ForeignKey(Buses, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        db_table = 'journeys'


class Passengers(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    assigned_journey = models.ForeignKey(Journeys, on_delete=models.CASCADE)

    class Meta:
        db_table = 'passengers'
