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
