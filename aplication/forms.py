from django import forms
from django.core import validators

class FormUser(forms.Form):
    nombre = forms.CharField(validators=[validators.MaxLengthValidator(5)])
    correo = forms.EmailField()
    opinion = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,
                                 widget=forms.HiddenInput)
    
    #Función para verificar que los datos en atrapabots están bien
    def clean_botcatcher(self):
        atrapador = self.cleaned_data['botcatcher']
        if (len(atrapador) > 0):
            raise forms.ValidationError("Ese mi EL BOT!")
        return atrapador
