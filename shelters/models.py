from django.db import models


# Create your models here.
class Address(models.Model):
    number = models.IntegerField()
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.IntegerField()


class Shelter(models.Model):
    name = models.CharField(max_length=50)
    address = models.ForeignKey(Address)
    allows_men = models.BooleanField()
    allows_women = models.BooleanField()
    allows_children = models.BooleanField()
    allows_couples = models.BooleanField()
    allows_pets = models.BooleanField()
    notes = models.CharField(max_length=1000)

