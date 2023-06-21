from cgitb import text
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'placeholder':'Escriba su nombrre','class':'form-control'}), min_length=3, max_length=100)
    email = forms.EmailField(label="Email", required=True,widget=forms.EmailInput(attrs={'placeholder':'Escriba su Email','class':'form-control'}), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(attrs={'class':'form-control','rows':3}))