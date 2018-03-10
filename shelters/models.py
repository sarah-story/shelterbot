from django.db import models
from address.models import AddressField


# Create your models here.

class Shelter(models.Model):
    name = models.CharField(max_length=200)
    address = AddressField()
    allows_men = models.BooleanField()
    allows_women = models.BooleanField()
    allows_children = models.BooleanField()
    allows_couples = models.BooleanField()
    allows_pets = models.BooleanField()
    notes = models.CharField(max_length=1000)
