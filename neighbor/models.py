from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
    LOCATIONS = (
    ('Westlands','Westlands',),
    ('Dagoretti','Dagoretti'),
    ('Kibra', 'Kibra'),
    ('Roysambu', 'Roysambu'),
    ('Kasarani', 'Kasarani'),
    ('Ruaraka', 'Ruaraka'),
    ('Embakasi', 'Embakasi'),
    ('Madaraka', 'Madaraka'),
    ('Kamukunji', 'Kamukunji'),
    ('Starehe', 'Starehe'),
    ('Mathare', 'Mathare'),
    )
    name = models.CharField(max_length = 30)
    location = models.CharField(max_length=50,choices=LOCATIONS)
    occupants = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.name
