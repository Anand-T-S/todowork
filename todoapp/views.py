from django.shortcuts import render,redirect
from todoapp.forms import TodoForm
from django.views.generic import View
from todoapp.models import Todos
todos=[

]


# Create your views here.

class TodoCreateView(View):
    def get(self,request):
        form=TodoForm()
        return render(request,"addtodo.html",{"form":form})
    def post(self,request):
        form=TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todos.objects.create(
                task_name=form.cleaned_data.get("task_name"),
                user=form.cleaned_data.get("user"),
                status=form.cleaned_data.get("status")
            )
            print("Todo Created")
            return redirect("alltodos")
        else:
            return render(request,"addtodo.html",{"form":form})

class TodoListView(View):
    def get(self,request):
        all_todos=Todos.objects.all()
        return render(request,"todolist.html",{"todos":all_todos})

class TodoFindView(View):
    def get(self,request):
        return render(request,"todo_detail.html")
    def post(self,request):
        id=int(request.POST.get("t_id"))
        todo=[todo for todo in todos if todo["id"]==id][0]
        return render(request,"todo_detail.html",{"todo":todo})

class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        todo=Todos.objects.get(id=id)
        return render(request,"details.html",{"todo":todo})

class TodoEditView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=[todo for todo in todos if todo["id"]==id][0]
        form=TodoForm(initial={"task_name":todo["title"],
                               "user":todo["userId"],
                               "completed_status":todo["completed"]

        })
        return render(request,"todo_edit.html",{"form":form})