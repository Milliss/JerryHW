from django.db import models

# Create your models here.
class graphh(models.Model):
	namee=models.CharField(max_length=87)
	discribe=models.CharField(max_length=87)
	picture=models.CharField(max_length=87)
	googleconnect=models.CharField(max_length=87)
	suggest=models.CharField(max_length=878)
	score=models.CharField(max_length=12)


	def __str__(self):
		return self.namee