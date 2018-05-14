from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Cherish
# Create your views here.
def index(request):
	cherr=Cherish.objects.all()
	return render_to_response('motherday/motherday.html',locals())