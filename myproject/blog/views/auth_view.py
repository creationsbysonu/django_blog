from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages


def renderRegisterForm(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create(
            username = username,
            email = email,
            password=password
        )
        # user.set_password(password)
        # user.save
        return redirect('/blog/login')

    else:
        return render(request,'auth/register.html')

def renderLoginForm(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            print("Invalid password")
            messages.error(request,"Invalid email or password")
            return redirect('/blog/login')
    return render(request,'auth/login.html')

def user_logout(request):
    logout(request)
    return redirect('login')