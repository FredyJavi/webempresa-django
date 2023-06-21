from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage
# Create your views here.

def contacto(request):
    contact_form=ContactForm() #se instancia para enviarlo en un diccionario
    if request.method == "POST":    
        contact_form=ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #para enviar correo
            email=EmailMessage(
                "quiero un pedido",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["fredy.moncaleano@gmail.com","fmonsa12@hotmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                #mensaje de envio en el caso que todo este bien
                return redirect(reverse('contacto')+"?ok") 
            except:
                #error que direcciona a fail
                return redirect(reverse('contacto')+"?fail") 
    return render(request,"contact/contacto.html",{'form':contact_form})