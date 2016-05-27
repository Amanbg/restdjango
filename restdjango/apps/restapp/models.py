from __future__ import unicode_literals

from django.db import models

# Create your models here.
class People(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	contact = models.CharField(max_length=10)
	emailid = models.CharField(max_length=40)
	created_on = models.DateTimeField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ('created_on',)




