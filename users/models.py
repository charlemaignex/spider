from django.db import models
from django.contrib.auth.models import User
from sms.models import Country
from decimal import Decimal

class Profile(models.Model):
	account_manager = models.ForeignKey(User, related_name='clientset')
	user = models.ForeignKey(User, unique=True)
	country = models.ForeignKey(Country)
	town_or_district = models.CharField(max_length=100,blank=True)
	phone_number = models.CharField(max_length=100)
	profit_ratio = models.DecimalField(max_digits=12,decimal_places=4,)# max_value=Decimal('1.0'))
	def __unicode__(self):
		return 'Profile for %s'%user
		
	def save(self,*args,**kwargs):
		# Each user must be updated with the manager's operators with the default %age added
		# Compare users' networks to admin's networks.
		# Add missing active networks with profit_ratio.
		# TO - DO
		super(Profile,self).save(*args,**kwargs)