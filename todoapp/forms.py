from django import forms
from todoapp.models import Todos

class TodoForm(forms.ModelForm):

    # date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
    options=(
        (True,True),
        (False,False)
    )
    status=forms.ChoiceField(choices=options)
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
            "status":forms.CheckboxInput(attrs={"class":"form-control"})
        }
