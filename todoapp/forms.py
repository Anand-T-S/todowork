from django import forms
from todoapp.models import Todos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):

    # date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
    # options=(
    #     (False,False),
    #     (True,True)
    # )
    # status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-select"}))
    class Meta:
        model=Todos
        fields=[
            "task_name"
        ]
        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"}),
            # "user":forms.Select(attrs={"class":"form-select"}),
        }

class UserRegistrationForm(UserCreationForm):
    # password1= forms.PasswordInput(),
    # "password2": forms.PasswordInput(attrs={"class": "form-control"}),
    class Meta:
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2"
        ]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),

        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))