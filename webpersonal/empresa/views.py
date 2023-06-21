from django.shortcuts import render,get_object_or_404,redirect
from .models import Page
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse,reverse_lazy


# Create your views here.

#@login_required()
def empresa(request):
    page = Page.objects.all() #pasa el identificador de la pagina y en caso de error 404
    if(not request.user.is_staff):
       return redirect(reverse_lazy('admin:login'))
    
    return render(request,"empresa/empresa.html", {'page':page})

# Create your views here.


