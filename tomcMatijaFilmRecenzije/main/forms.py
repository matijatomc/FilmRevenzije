from django import forms
from .models import Recenzija

class RecenzijaForm(forms.ModelForm):
    class Meta:
        model = Recenzija
        fields = ['ocjena', 'recenzija']