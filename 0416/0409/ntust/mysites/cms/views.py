from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Restaurant,Food,Namess
# Create your views here.
def index(request):
	restaurants=Restaurant.objects.all()
	myname=Namess.objects.all()
	return render_to_response('cms/menu.html',locals())

