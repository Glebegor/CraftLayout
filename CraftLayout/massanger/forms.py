from dataclasses import field
from django import forms
from .models import MassangerModel

class massangerForm(forms.ModelForm):
    class Meta:
        model = MassangerModel
        fields = '__all__'
