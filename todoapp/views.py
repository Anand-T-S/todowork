from django.shortcuts import render
from todoapp.forms import TodoForm
from django.views.generic import View

# Create your views here.

class TodoCreateView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,"addtodo.html",{"form":form})
    def post(self,request):
        form=TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request,"addtodo.html",{"form":form})
        else:
            return render(request,"addtodo.html",{"form":form})
