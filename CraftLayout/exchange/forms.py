from django import forms
from django.forms import ModelForm
from dataclasses import fields
from pyexpat import model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Exchange

class FormExchange(ModelForm):
    title = forms.CharField(required=True)
    salary = forms.CharField(required=True)
    text = forms.Textarea()
    technologies = forms.CharField(required=True)
    class Meta:
        model = Exchange
        fields = ['title','salary','text', 'technologies', 'id']

