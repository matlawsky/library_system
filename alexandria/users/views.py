from django.shortcuts import render

def signup(request):
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