from dataclasses import field
from tkinter import Label, Widget
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django import forms
from .models import *
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class PostForm(forms.Form):
    name = forms.CharField(max_length=20, label="Nome")
    text = forms.CharField(widget=forms.Textarea, label="Mensagem")
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox, label=False)

    
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise ValidationError('Nome precisa ter pelo menos dois caracteres!')
        else:
            return name

    def clean_text(self):
        text = self.cleaned_data['text']
        if len(text) < 5:
            raise ValidationError('texto muito curto!')
        else:
            return text
