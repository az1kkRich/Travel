from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages 
# Create your views here.

def register(request):

    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['pas1']

        password2=request.POST['pas2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'login olingan, boshqa login kiriting')
                return render(request, 'register.html')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Bor Qayta kiriting:')
                return render(request, 'register.html')

            else:
                user=User.objects.create_user(username=username, email=email, password=password)
                user.save();

        else:
            messages.info(request, 'parol bir xil emas')
            return render(request, 'register.html')
        return redirect('/')


    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'login yoki parol xato')
            return render(request, 'Login.html')



    return render(request, 'Login.html')

def logout(request):
    auth.logout(request)
    return  redirect('/')

    