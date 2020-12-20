from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	#return HttpResponse("<em>Hello World!</em>")
	my_dict ={'insert_me':"Now iam coming from first_app/index.html !"}
	return render(request,'first_app/index.html',context=my_dict)

def help(request):
	my_dict ={'help_me':"We are here to help you bro!"}
	return render(request,'first_app/help.html',context=my_dict)
