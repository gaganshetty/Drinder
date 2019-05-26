from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime

class Location(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Restaurant(models.Model):
	name = models.CharField(max_length=20)
	location = models.ForeignKey(Location,on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Cusine(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name


class Person(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio = models.CharField(max_length=50, blank=True)
	is_available = models.DateField(blank=True, null=True)
	location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True, null=True)
	

	def __str__(self):
		return self.user.first_name
		
	def is_available_today(self):
		 self.is_available = datetime.now()
		 self.save()
		 return self.is_available
