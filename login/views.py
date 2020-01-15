from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
# Create your views here.
def login(request):
	if request.method == 'POST':
		user_name = request.POST['user_name']
		password = request.POST['password']
		user = auth.authenticate(username=user_name, password=password)
		print(user_name)
		if user is not None :
			return (redirect('/'))
		else:
			messages.info(request,'invalid credentials')
			return (redirect('/login'))

	else:
		return render(request,'login/login.html')