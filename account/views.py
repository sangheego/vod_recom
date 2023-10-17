from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def custom_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success.html')
        else:
            messages.error(request, '올바른 아이디가 아닙니다.')
    return render(request, 'login.html')

def custom_logout(request):
    auth.logout(request)
    return redirect('home')

def success(request):
    return render(request, 'success.html')