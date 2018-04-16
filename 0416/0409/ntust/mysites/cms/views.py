from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Restaurant,Food
# Create your views here.
def index(request):
	restaurants=Restaurant.objects.all()
	return render_to_response('cms/menu.html',locals())
	