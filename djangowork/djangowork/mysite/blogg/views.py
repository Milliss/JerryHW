from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Names
# Create your views here.
def index(request):
	myname=Names.objects.all()
	return render_to_response('blogg/blog.html',locals())