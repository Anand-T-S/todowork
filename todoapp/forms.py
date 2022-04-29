from django import forms
from todoapp.models import Todos
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.ModelForm):

    # date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
    options=(
        (True,True),
        (False,False)
    )
    status=forms.ChoiceField(choices=options,widget=forms.Select(attrs={"class":"form-select"}))
    class Meta:
        model=Todos
        fields=[
            "task_name",
            "user",
            "status"
        ]
        widgets={
            "task_name":forms.TextInput(attrs={"class":"form-control"}),
            "user":forms.TextInput(attrs={"class":"form-control"}),
        }

class UserRegistrationForm(UserCreationForm):
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

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)