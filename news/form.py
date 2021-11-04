from django import forms
class loginForm(forms.Form):
    username = forms.CharField(max_length=300,required=True)
    password = forms.CharField(max_length= 300,required=True)

class registerForm(forms.Form):
    username = forms.CharField(max_length=300,required=True)
    password = forms.CharField(max_length= 300,required=True)
    address = forms.CharField(max_length=500,required=True)
    phone = forms.FloatField(required=True)

