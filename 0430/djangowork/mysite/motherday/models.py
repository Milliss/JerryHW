from django.db import models

# Create your models here.
class Cherish(models.Model):
	cherich=models.CharField(max_length=87)

	def __str__(self):
		return self.cherich