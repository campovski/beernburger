from django.db import models
from datetime import datetime


class Country(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Manufacturer(models.Model):
	name = models.CharField(max_length=200)
	country = models.ForeignKey(Country)

	def __str__(self):
		return self.name


class Beer(models.Model):
	name = models.CharField(max_length=300)
	review = models.CharField(max_length=5000)
	beer_type = models.CharField(max_length=30)
	grade_taste = models.CharField(max_length=1)
	grade_color = models.CharField(max_length=1)
	grade_smell = models.CharField(max_length=1)
	grade_smoothness = models.CharField(max_length=1)
	grade_foam = models.CharField(max_length=1)
	grade_total = models.CharField(max_length=1)
	alc = models.CharField(max_length=4)
	image = models.CharField(max_length=100)
	image_tile = models.CharField(max_length=100)
	brewer = models.ForeignKey(Manufacturer)
	price = models.CharField(max_length=10)
	date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.name + ' - ' + str(self.brewer)
