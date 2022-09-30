from django.db import models

class Staff(models.Model):
	Name=models.CharField(max_length=50)
	Department=models.CharField(max_length=50)
	Contact=models.CharField(max_length=50)
# Create your models here.
