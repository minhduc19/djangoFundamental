from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('<p>In index View</p>')

def item_detail(request,id):
	response =  HttpResponse()
	response.write('<p>In item_detail view with id {0}</p>'.format(id))
	#return HttpResponse(id)
	return response


# Create your views here.
