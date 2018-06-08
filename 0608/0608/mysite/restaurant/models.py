from django.db import models

# Create your models here.
class Restaurant(models.Model):
	name=models.CharField(max_length=87)
	tele=models.CharField(max_length=11)
	address=models.CharField(max_length=87,blank=True)
	googlecon=models.URLField(blank=True)

	def __str__(self):
		return self.name


class Picture(models.Model):
	name=models.CharField(max_length=87)
	pic=models.URLField(blank=True)
	restaurant=models.ForeignKey(Restaurant)

	def __str__(self):
		return self.name
