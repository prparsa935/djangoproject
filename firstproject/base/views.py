from django.shortcuts import render


def ShowMain(request):
    return render(request,"home.html")

