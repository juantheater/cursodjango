from django.shortcuts import render,redirect
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.
def contacto(request):
    formu_contac=FormularioContacto

    if request.method=='POST':
        formu_contac=FormularioContacto(data=request.POST)

        if formu_contac.is_valid():
            nombre=request.POST.get('nombre')
            email=request.POST.get('email')
            contenido=request.POST.get('contenido')

            email=EmailMessage("Mensaje desde App Contacto:",
                               "El usuario con nombre {}, con la dirección {}, escribe: {}"
                               .format(nombre,email,contenido),"",['jctpicon@gmail.com'],
                               [email])
            try:
                email.send()
                return redirect("/contacto/?valido")
            except:
                return redirect("/contacto/?novalido")
    
    return render(request,'Contactos/contacto.html',{'miformulario':formu_contac})