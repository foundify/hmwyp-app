from django.conf import settings
from django.db import models
from django.utils import timezone
from django import forms

# Create your models here.

class VintageMac(models.Model):
	price = models.IntegerField()

	def publish(self):
		self.save()

	def __str__(self):
		return '%s' % (self.price)

class Nike(models.Model):
	price = models.IntegerField()


	def publish(self):
		self.save()

	def __str__(self):
		return '%s' % (self.price)

class Parking(models.Model):
	price = models.IntegerField()


	def publish(self):
		self.save()

	def __str__(self):
		return '%s' % (self.price)

class Milk(models.Model):
	price = models.IntegerField()


	def publish(self):
		self.save()

	def __str__(self):
		return '%s' % (self.price)

class Money(models.Model):
	price = models.IntegerField()


	def publish(self):
		self.save()

	def __str__(self):
		return '%s' % (self.price)
