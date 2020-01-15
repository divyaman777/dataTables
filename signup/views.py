from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
	if request.method == 'POST':
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		user_name = request.POST['user_name']
		email = request.POST['email']
		password = request.POST['password']

		user = User.objects.create_user(username=user_name, password=password, email=email, first_name=first_name, last_name=last_name)
		user.save();
		print('User Created!!')
		return (redirect('/login'))
	else:
		return render(request,'signup/signup.html')
