from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Names,Question
# Create your views here.
def index(request):
	myname=Names.objects.all()
	ques=Question.objects.all()
	return render_to_response('blogg/blog.html',locals())

def detail(request,question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request,question_id):
	response="You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request,question_id):
	return HttpResponse("You're voting on question %s." % question_id)

