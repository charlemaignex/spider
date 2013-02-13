#We should be able to get an SMS sent through the most reliable and economic route

from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime, timedelta
from decimal import Decimal

class Contact(models.Model):
	name = models.CharField(max_length=25, blank=True)
	number = models.IntegerField()
	def __unicode__(self):
		if self.name:name=' - %s'%self.name
		else:name = ''
		return '%s%s'%(self.number,name)
	

class SMS(models.Model):
	user = models.ForeignKey(User,unique=True)
	contacts = models.ManyToManyField(Contact)
	text = models.CharField(max_length=160*6)
	send_at = models.DateTimeField(default=datetime.now())
	created_at = models.DateTimeField(auto_now_add=True)
	is_sent = models.BooleanField(default=False)
	def __unicode__(self):
		return '%s'%self.text
	def send(self,request):
		pass
		
class Country(models.Model):
	name = models.CharField(max_length=100)
	code = models.CharField(max_length=5)

class Route(models.Model):
	getter_name = models.CharField(max_length=100)
	destinations = models.ManyToManyField(Country)
	default_price = models.DecimalField(max_digits=12,decimal_places=4)
	is_active = models.BooleanField(default=False)
	
class Operator(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=100)
	country = models.ForeignKey(Country)
	price = models.DecimalField(max_digits=12,decimal_places=4, default = Decimal('0.0000'))
	is_active = models.BooleanField(default=False)
	# Each user has all the available networks from the admin
	#The defaul price is the price of their admin's price + a set percentage
	# An admin can set a price for each of their users' networks