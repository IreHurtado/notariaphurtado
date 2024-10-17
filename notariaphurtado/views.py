from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "general/home.html"
    
class NosotrosView(TemplateView):
    template_name = "general/nosotros.html"
    
def contact_view(request):
    if request.method == 'POST':  
        formulario = ContactForm(request.POST)
        
        if formulario.is_valid():
            # Obtener los datos del formulario
            nombre = formulario.cleaned_data['nombre']
            email = formulario.cleaned_data['email']
            telefono = formulario.cleaned_data['telefono']
            mensaje = formulario.cleaned_data['mensaje']
            
            # Imprimir los datos en la consola para verificar
            print(f'{nombre} con {telefono} ha enviado un correo procedente de email {email} con el texto: {mensaje}')
            
            # Enviar el correo
            subject = f'Nuevo mensaje de {nombre}'
            message = f'Nombre: {nombre}\nEmail: {email}\nTeléfono: {telefono}\nMensaje: {mensaje}'
            from_email = email  # Opcionalmente puedes usar un correo predefinido aquí
            recipient_list = ['informes@notariaphurtado.com']
            
            try:
                send_mail(subject, message, from_email, recipient_list)
                messages.success(request, 'El formulario se ha enviado correctamente.')
                return redirect('contacto')
            except Exception as e:
                messages.error(request, f'Error al enviar el formulario: {str(e)}')
            
            # Redirigir después de un envío exitoso
            return redirect('contacto')
    else:
        formulario = ContactForm()

    context = {
        'formulario': formulario
    }
    
    return render(request, "general/contacto.html", context)