from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import graphh
# Create your views here.
def index(request):
	mygraphh=graphh.objects.all()
	return render_to_response('blog/blog.html',locals())
