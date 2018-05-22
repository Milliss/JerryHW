from django.db import models

# Create your models here.
class graphh(models.Model):#graph功能
	namee=models.CharField(max_length=87)
	discribe=models.CharField(max_length=87)
	picture=models.CharField(max_length=87)
	googleconnect=models.CharField(max_length=87)
	suggest=models.CharField(max_length=878)
	score=models.CharField(max_length=12)
	telephone=models.DecimalField(max_digits=11,decimal_places=0)
	place=models.CharField(max_length=87)

	def __str__(self):
		return self.namee

class Post(models.Model):#回饋系統
    title = models.CharField(max_length=200)
    score =models.DecimalField(max_digits=7,decimal_places=0)
    content = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
    def __str__(self):
        return self.title