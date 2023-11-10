from django.db import models

# Create your models here.

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    location = models.URLField(max_length=200)
    open_time = models.TimeField()
    close_time = models.TimeField()
    coffee_rating = models.IntegerField()
    wifi_rating = models.IntegerField()
    power_outlets = models.IntegerField()
    
    def __str__(self):
        return self.name 