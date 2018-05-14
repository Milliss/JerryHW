from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Names(models.Model):
	namee=models.CharField(max_length=87)
	nickname=models.CharField(max_length=87)
	birthdayy=models.DecimalField(max_digits=7,decimal_places=0)
	constellation=models.CharField(max_length=87)
	sexs=models.CharField(max_length=2)
	stunumber=models.CharField(max_length=12)


	def __str__(self):
		return self.namee

class Question(models.Model):
	question_text=models.CharField(max_length=200)
	pub_date=models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title