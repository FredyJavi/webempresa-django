from django.shortcuts import render,HttpResponse
from .models import redsocial
# Create your views here.

def home(request):
    return render(request,"core/home.html")

def about(request):
    return render(request,"core/about.html")


def base(request):
   rsocial=redsocial.objects.all()
   return render(request,"core/base.html",{'rsocial':rsocial})