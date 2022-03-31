from django.shortcuts import render


def ShowMain(request):
    return render(request,"home.html")


def login_page(request):
    return render(request,"login.html")
