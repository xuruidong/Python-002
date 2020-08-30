from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Hello Django!")
	

def re_year(request, year):
	return render(request, 'yearview.html')


def myint(request, year):
	# return HttpResponse(year+10)
	return redirect("http://www.baidu.com")
