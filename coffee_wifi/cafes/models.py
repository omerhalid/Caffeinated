from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    location = models.URLField(max_length=200)
    open_time = models.TimeField(help_text='24 hour format')
    close_time = models.TimeField(help_text='24 hour format')
    coffee_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], help_text='1-10')
    wifi_rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], help_text='1-10')
    power_outlets = models.IntegerField(help_text='Number of power outlets available')
    
    def __str__(self):
        return self.name 
    