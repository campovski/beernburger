from django.db import models
from beer.models import Manufacturer


class Torc(models.Model):
	name = models.CharField(max_length=200)
	maker = models.ForeignKey(Manufacturer)
	review = models.CharField(max_length=3000)
	grade_total = models.CharField(max_length=1)
	grade_taste = models.CharField(max_length=1)
	grade_smell = models.CharField(max_length=1)
	grade_color = models.CharField(max_length=1)
	how_strong = models.CharField(max_length=1)
	image = models.CharField(max_length=100)
	image_tile = models.CharField(max_length=100)
