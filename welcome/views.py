from django.shortcuts import render
from django.template import loader
# Create your views here.

# from django.http import HttpResponse

def index(request):
	context = {}
	return render(request,'welcome/index.html',context)
