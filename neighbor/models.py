from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
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

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    def update_neighborhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()
