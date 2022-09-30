from django.db import models

class Category(models.Model):
	"""Categories for the items i.e Food, Home"""
	Name=models.CharField(max_length=50)

	def __str__(self):
		return self.Name
	class Meta:
		ordering=['Name']

class Item(models.Model):
	"""Class Item stores information on each item."""
	Category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	Name=models.CharField(max_length=50)
	Measure=models.CharField(max_length=50)

	def __str__(self):
		return self.Name

class Userdetail(models.Model):
	"""Details of the users e.g their phone number"""
	Contact=models.CharField(max_length=20)
	Firstname=models.CharField(max_length=50)
	Secondname=models.CharField(max_length=50)
	Status=models.CharField(max_length=50)

	def __str__(self):
		return self.Firstname

class Biz(models.Model):
	"""This will store information of the clients business for accurate deliveries"""
	Name=models.CharField(max_length=50)
	Location=models.TextField()
	Owner=models.ForeignKey(Userdetail, on_delete=models.CASCADE)
	Fee=models.IntegerField(default=50,)
	def __str__(self):
		return self.Name
	class Meta:
		ordering=['Name']
class Brand(models.Model):
	Name=models.CharField(max_length=50, null=True)
	Item=models.ForeignKey(Item, on_delete=models.CASCADE)
	Category=models.ForeignKey(Category, models.CASCADE, default='1')
	Bought=models.IntegerField()
	Sold=models.IntegerField()
	Instock=models.BooleanField()
	Quantity=models.IntegerField()
	Pic=models.ImageField(upload_to='pictures', null=True)
	Discount=models.IntegerField(null=True)

	def __str__(self):
		return self.Name

	class Meta:
		ordering=['Name']
class Cart(models.Model):
	Session=models.CharField(max_length=60)
	Total=models.FloatField(null=True)
	def __str__(self):
		return self.Session

		
class Order(models.Model):
	Cart=models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
	Brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
	Quantity=models.IntegerField()
	Bill=models.FloatField(null=True)
	User=models.ForeignKey(Userdetail, on_delete=models.CASCADE, null=True)
	Wakati=models.DateTimeField()
	Status=models.CharField(max_length=50, null=True)
	class Meta:
		ordering=['User']
		
class Delivery(models.Model):
	Cart=models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
	Status=models.CharField(max_length=60)
	Location=models.TextField()
	Ordertime=models.DateTimeField(null=True)
	Deltime=models.TimeField(null=True)

		





# Create your models here.
