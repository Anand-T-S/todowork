from django import forms

class TodoForm(forms.Form):
    task_name=forms.CharField()
    user=forms.CharField()
    date=forms.DateField()
    completed_status=forms.BooleanField()
