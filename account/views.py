from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')
        else:
            messages.error(request, '올바른 아이디가 아닙니다.')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')