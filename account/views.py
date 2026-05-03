from django.shortcuts import render

# Create your views here.

def Signup(request):
    return render(request, 'signup.html')


def Login(request):
    return render(request, 'login.html')

def Forget_password(request):
    return render(request, 'forget_password.html')

def Reset_password(request):
    return render(request, 'reset_password.html')
