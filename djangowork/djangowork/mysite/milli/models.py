from django.db import models

# Create your models here.
class Namess(models.Model):
	namee=models.CharField(max_length=87)
	nickname=models.CharField(max_length=87)
	birthdayy=models.DecimalField(max_digits=7,decimal_places=0)
	constellation=models.CharField(max_length=87)
	sexs=models.CharField(max_length=2)
	stunumber=models.CharField(max_length=12)


	def __str__(self):
		return self.namee