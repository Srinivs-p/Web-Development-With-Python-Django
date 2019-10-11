from django.db import models

# Create your models here.

class form(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.CharField(max_length=255)
	phone = models.CharField(max_length=255)
	Message = models.CharField(max_length=500)