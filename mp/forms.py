from .models import Messageprive
from django import forms

class MessageForms(forms.ModelForm):

    class Meta:
        model = Messageprive
        fields = ['title' , 'text' , 'receiver']