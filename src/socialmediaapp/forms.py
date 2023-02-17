from django import forms
from django.contrib.auth.models import User

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label = 'password',
        widget = forms.PasswordInput(
            attrs = {
            'placeholder':'Password',
            'class':'form-control'
            }
        )
    )
    confirmpassword = forms.CharField(
        label = 'Confirm-password',
        widget = forms.PasswordInput(
            attrs = {
            'placeholder':'Confirm-Password',
            'class':'form-control'
            }
        )
    )
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username']


class UserLoginForm(forms.Form):
    username = forms.CharField(
    label = 'UserName',
    widget = forms.TextInput(
        attrs = {
            'placeholder':'Username',
            'class':'form-control'
        }
    )
    )
    password = forms.CharField(
    label = 'PassWord',
    widget = forms.PasswordInput(
        attrs = {
        'placeholder':'PassWord',
        'class':'form-control'
        }
    )
    )


class ArticlecreateForm(forms.Form):
    title = forms.CharField(
        label = 'Enter Title',
        widget = forms.TextInput(
            attrs = {
            'placeholder':'title......',
            'class':'form-control'
            }
        )

    )

    body = forms.CharField(
        label = 'Enter Body',
        widget = forms.Textarea(
            attrs = {
            'placeholder':'Body......',
            'class':'form-control',
            'rows':5,
            'columns':50

            }
        )
    )




#
