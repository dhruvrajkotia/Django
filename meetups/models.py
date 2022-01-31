from operator import mod
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f'{self.name} ({self.address})'


class Participent(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self) -> str:
        return self.email

class Meetup(models.Model):
    title = models.CharField(max_length=200)
    organizeer_email = models.EmailField()
    date = models.DateField()
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    participents =  models.ManyToManyField(Participent, blank=True, null=True)
