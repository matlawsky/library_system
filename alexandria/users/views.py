from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        # the user wants to sign up

            if request.POST.get('password') == request.POST.get('passwordCheck'):
                try:
                    user = User.objects.get(username=request.POST.get('userName'))
                    return render(request, 'users/signup.html', {'error': 'Username has already been taken!'})
                except User.DoesNotExist:
                    user = User.objects.create_user(
                    username=request.POST.get('userName'),
                    password=request.POST.get('password'),
                    email=request.POST.get('email'),
                    first_name= request.POST.get('firstName'),
                    last_name=request.POST.get('lastName'),
                    )
                    auth.login(request,user)
                    return redirect('home')
            else:
                return render(request, 'users/signup.html', {'error': 'Passwords do not match!'})               

    else: 
        # user wants to enter info
        return render(request, 'users/signup.html')

def login(request):
    return render(request, 'users/login.html')

def logout(request):
    # TODO  need to route to homepage
    # and don't forget to logout
    render(request, 'users/logout.html')

def myaccount(request):
    return render(request, 'users/myaccount.html')

def mybooks(request):
    return render(request, 'users/mybooks.html')