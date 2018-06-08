from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from .models import Restaurant,Picture

def index(request):
	restaurants=Restaurant.objects.all()
	picture=Picture.objects.filter(restaurant=restaurants)
	return render(request,'restaurant.html',locals())