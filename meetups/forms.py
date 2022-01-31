from django import forms
from .models import Participent

class RegistrationForms(forms.Form):
    email = forms.EmailField(label='Your Email')
