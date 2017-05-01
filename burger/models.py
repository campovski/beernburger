from django.db import models
from beer.models import Manufacturer


class Burger(models.Model):
	name = models.CharField(max_length=200)
	maker = models.ForeignKey(Manufacturer)
	review = models.CharField(max_length=5000)
	grade_total = models.CharField(max_length=1)
	grade_taste = models.CharField(max_length=1)
	grade_appearance = models.CharField(max_length=1)
	juicyness = models.CharField(max_length=1)
	spicyness = models.CharField(max_length=1)
	image = models.CharField(max_length=100)
	image_tile = models.CharField(max_length=100)
