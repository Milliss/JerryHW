from django.shortcuts import render_to_response,render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.
def index(request):
	mygraphh=graphh.objects.all()
	ques=Question.objects.all()
	return render_to_response('blog/blog.html',locals())

def blog(request):
	if request.method == 'POST':
		pk = request.POST.get('pk')
		Post.objects.get(pk=pk).delete()
	post_list = Post.objects.all()
	return render(request, 'blog/blog.html', {'post_list': post_list})

def new(request):
	if request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		Post.objects.create(title=title, content=content)
		return redirect('/blog')
	return render(request, 'blog/new.html')

def edit(request):
	pk = request.GET.get('q')
	post = Post.objects.get(pk=pk)
	if request.method == 'POST':
		post.title = request.POST.get('title')
		post.content = request.POST.get('content')
		post.save()
		return redirect('/blog')
	return render(request, 'blog/edit.html', {'post': post})

def menu(request):
	return render_to_response('blog/menu.html',locals())