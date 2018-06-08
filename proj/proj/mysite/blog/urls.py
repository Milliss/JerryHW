from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.blog, name='blog'),
    url(r'^new/', views.new, name="new"),
    url(r'^edit/', views.edit, name="edit"),
    url(r'^menu/', views.menu, name="menu"),
    url(r'^restaurant/', views.restaurant, name="restaurant"),

]