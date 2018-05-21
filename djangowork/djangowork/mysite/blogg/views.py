from django.shortcuts import render_to_response,render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Names,Question
# Create your views here.
def index(request):
	myname=Names.objects.all()
	ques=Question.objects.all()
	return render_to_response('blogg/blog.html',locals())

def new(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		Post.objects.create(title=title, content=content)
		return redirect('/blog')
	return render(request, 'new.html')

def edit(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()
		return redirect('/blog')
	return render(request, 'edit.html', {'post': post})