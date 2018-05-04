from django.shortcuts import render_to_response
from django.http import HttpResponse
from .models import Namess
# Create your views here.
def index(request):
	mynamee=Namess.objects.all()
	return render_to_response('milli/mypage.html',locals())