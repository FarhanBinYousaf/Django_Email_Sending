from .models import Form
from django import forms
from django.contrib.auth.forms import UserCreationForm

class MailForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = ['name','fatherName','email','msg']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'fatherName':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'msg':forms.TextInput(attrs={'class':'form-control'})
            }
        labels = {
            'name':'Username',
            'fatherName':'Father Name',
            'email':'Your Email',
            'msg':'Subject*',
        }