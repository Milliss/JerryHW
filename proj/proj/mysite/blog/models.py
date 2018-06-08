from django.db import models

# Create your models here.
class restaurant(models.Model):
	Name=models.CharField(max_length=87)
	Telephone=models.DecimalField(max_digits=10,decimal_places=0)
	Address=models.CharField(max_length=87)
	googleconnect=models.CharField(max_length=887)

	def __str__(self):
		return self.Name

class picture(models.Model):
	Name=models.CharField(max_length=87)
	hreflink=models.CharField(max_length=887)
	
	def __str__(self):
		return self.Name

class Post(models.Model):#回饋系統
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')
    
    def __str__(self):
        return self.title