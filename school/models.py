from django.db import models
from django.conf import settings


class SchoolPost(models.Model):
	block 				= models.CharField(max_length=50, null=False, blank=False)
	cluster 			= models.TextField(max_length=5000, null=False, blank=False)
	schoolid 			= models.IntegerField(null=False, blank=False)
	schoolname 			= models.CharField(max_length=100, null=False, blank=False)
	category			= models.CharField(max_length=50, null=False, blank=False)
	gender				= models.CharField(max_length=50, null=False, blank=False)
	medium_of_inst 		= models.CharField(max_length=50, null=False, blank= False)
	address				= models.CharField(max_length=500, null=False, blank=False)
	area				= models.CharField(max_length=50, null=False, blank=False)
	pincode				= models.IntegerField(null=False, blank=False)
	landmark 			= models.CharField(max_length=50, null=False, blank=False)
	busroutes			= models.CharField(max_length=500, null=False, blank=False)

	def __str__(self):
		return self.title

