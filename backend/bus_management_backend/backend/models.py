from glob import escape
from django.db import models



class Drivers(models.Model):
    driver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, null=False, blank=False)
    last_name = models.CharField(max_length=20, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)

    class Meta:
        db_table = 'drivers'

class Buses(models.Model):
    bus_id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=7, unique=True)
    years_of_service = models.IntegerField()
    capacity = models.IntegerField(default=10, null=False)
    driver = models.OneToOneField(Drivers, on_delete=models.CASCADE, null=False, unique=True) 

    class Meta:
        db_table = 'buses'
 
class Journeys(models.Model):
    journey_id = models.AutoField(primary_key=True)
    journey_name = models.CharField(max_length=10, unique=True)  
    from_city = models.CharField(max_length=50, default='' )
    to_city = models.CharField(max_length=50, default='')
    buses = models.ManyToManyField(Buses)
    date = models.DateTimeField()
    class Meta:
        db_table = 'journeys'


class Passengers(models.Model):
    passenger_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    journey = models.ForeignKey(Journeys, on_delete=models.CASCADE)
    bus = models.ForeignKey(Buses, on_delete=models.CASCADE, default=1)
    
    class Meta:
        db_table = 'passengers'
