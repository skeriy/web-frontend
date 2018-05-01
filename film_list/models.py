from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Films(models.Model):
    film_name = models.CharField(max_length=100)
    release_date = models.DateField()
    director = models.CharField(max_length=100)
    duration = models.CharField(max_length=20)
    rating = models.IntegerField(default=1, validators=[MaxValueValidator(10),MinValueValidator(1)])
