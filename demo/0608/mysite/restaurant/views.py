from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from .models import *

def index(request):
	restaurants=Restaurant.objects.all()
	return render(request,'restaurant1.html',locals())

def index2(request):
	restaurants2=Restaurant2.objects.all()
	return render(request,'restaurant2.html',locals())

def categorize(request):
	return render(request,'categorize.html',locals())

def lottery(request):
	return render(request,'lottery.html',locals())

def chinese(request):
	return render(request,'chinese.html',locals())	

def japanese(request):
	return render(request,'japanese.html',locals())

def korean(request):
	return render(request,'korean.html',locals())

def southeast(request):
	return render(request,'southeast.html',locals())

def american(request):
	return render(request,'american.html',locals())

def euro(request):
	return render(request,'euro.html',locals())	

def homepage(request):
	return render(request,'homepage.html',locals())

def index3(request):
	restaurants3=Restaurant3.objects.all()
	return render(request,'restaurant3.html',locals())

def index4(request):
	restaurants4=Restaurant4.objects.all()
	return render(request,'restaurant4.html',locals())

def index5(request):
	restaurants5=Restaurant5.objects.all()
	return render(request,'restaurant5.html',locals())

def index6(request):
	restaurants6=Restaurant6.objects.all()
	return render(request,'restaurant6.html',locals())

def index7(request):
	restaurants7=Restaurant7.objects.all()
	return render(request,'restaurant7.html',locals())

def index8(request):
	restaurants8=Restaurant8.objects.all()
	return render(request,'restaurant8.html',locals())

def index9(request):
	restaurants9=Restaurant9.objects.all()
	return render(request,'restaurant9.html',locals())

def index10(request):
	restaurants10=Restaurant10.objects.all()
	return render(request,'restaurant10.html',locals())

def index11(request):
	restaurants11=Restaurant11.objects.all()
	return render(request,'restaurant11.html',locals())

def index12(request):
	restaurants12=Restaurant12.objects.all()
	return render(request,'restaurant12.html',locals())

def index13(request):
	restaurants13=Restaurant13.objects.all()
	return render(request,'restaurant13.html',locals())

def index14(request):
	restaurants14=Restaurant14.objects.all()
	return render(request,'restaurant14.html',locals())

def index15(request):
	restaurants15=Restaurant15.objects.all()
	return render(request,'restaurant15.html',locals())

def index16(request):
	restaurants16=Restaurant16.objects.all()
	return render(request,'restaurant16.html',locals())

def index17(request):
	restaurants17=Restaurant17.objects.all()
	return render(request,'restaurant17.html',locals())

def index18(request):
	restaurants18=Restaurant18.objects.all()
	return render(request,'restaurant18.html',locals())

def index19(request):
	restaurants19=Restaurant19.objects.all()
	return render(request,'restaurant19.html',locals())

def index20(request):
	restaurants20=Restaurant20.objects.all()
	return render(request,'restaurant20.html',locals())

def index21(request):
	restaurants21=Restaurant21.objects.all()
	return render(request,'restaurant21.html',locals())

def index22(request):
	restaurants22=Restaurant22.objects.all()
	return render(request,'restaurant22.html',locals())

def index23(request):
	restaurants23=Restaurant23.objects.all()
	return render(request,'restaurant23.html',locals())

def index24(request):
	restaurants24=Restaurant24.objects.all()
	return render(request,'restaurant24.html',locals())






