from django import forms

class TodoForm(forms.Form):
    task_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    user=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # date=forms.DateField(widget=forms.DateInput(attrs={"class":"form-control","type":"date"}))
    options=(
        (True,True),
        (False,False)
    )
    status=forms.ChoiceField(choices=options)
