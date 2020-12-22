from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
	webpages_list=AccessRecord.objects.order_by('date')
	date_dict={'access_records': webpages_list}
	#return HttpResponse("<em>Hello World!</em>")
	return render(request,'first_app/index.html',context=date_dict)

def webpagedata(request):
	wp=Webpage.objects.order_by('name')
	my_dict={'records':wp}
	return render(request,'first_app/webpagedata.html',context=my_dict)
