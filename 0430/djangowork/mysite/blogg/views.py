from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
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

def blog(request):
	if request.method == 'POST':
		pk = request.POST.get('pk')
		Post.objects.get(pk=pk).delete()
	post_list = Post.objects.all()
	return render(request, 'blogg/blog.html', {'post_list': post_list})

def new(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		Post.objects.create(title=title, content=content)
		return redirect('/blogg')
	return render(request, 'blogg/new.html')

def edit(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()
		return redirect('/blogg')
	return render(request, 'blogg/edit.html', {'post': post})