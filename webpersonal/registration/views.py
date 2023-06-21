from .forms import UserCreationEmail
#from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

class SigUpView (CreateView):
    form_class=UserCreationEmail
    template_name='registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login')+'?register' #redirigir al login despues del registro()

    def get_form(self, form_class=None) :
        form=super(SigUpView,self).get_form()
        form.fields['username'].widget=forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Nombre de usuario'})
        form.fields['email'].widget=forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Correo@valido.com'})
        form.fields['password1'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Contraseña'})
        form.fields['password2'].widget=forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Confirmar Contraseña'})
        
        form.fields['username'].label='' # ocultar los label
        form.fields['password1'].label=''
        form.fields['password2'].label=''
        return form

# Create your views here.
