from django.shortcuts import render


def renderHomePage(request):
    return render(request,'home/homepage.html')