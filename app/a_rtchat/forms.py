from django.forms import ModelForm
from django import forms
from .models import *


class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder':'Add message ...', 'class': 'p-4 text-black', 'maxlength': '300', 'autofocus': True, 'autocomplete': 'off'})
        }
        

class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'placeholder':'Add name ...', 
                'class': 'p-4 text-black', 
                'maxlength': '128',
                'autofocus': True
                })
        }
        
class ChatGroupEditForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'class': 'p-4 text-xl font-bold mb-4', 
                'maxlength': '300'
                }),
        }