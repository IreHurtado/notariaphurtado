from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=140, label="Nombre y Apellidos")
    email = forms.EmailField(label="Email")
    telefono = forms.CharField(max_length=11, label="Teléfono", 
                               error_messages={'max_length': 'El teléfono no puede exceder los 11 caracteres.'})
    mensaje = forms.CharField(max_length=1000, label="Mensaje", widget=forms.Textarea)
    
    def clean_mensaje(self):
        mensaje = self.cleaned_data.get('mensaje')  
        if len(mensaje) < 5:
            raise forms.ValidationError("El mensaje debe tener al menos 5 caracteres")
        return mensaje

    def clean_telefono(self):
        telefono = self.cleaned_data.get('telefono')
        if not telefono.isdigit():  
            raise forms.ValidationError("El teléfono debe contener solo números.")
        return telefono