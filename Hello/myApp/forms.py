from django import forms
from .models import Hello

class FormContactForm(forms.ModelForm):
    class Meta:
        model= Hello
        fields= ["firstname", "lastname", "gender", "email", "password"]
