from django.shortcuts import render,redirect
from todoapp.forms import TodoForm,UserRegistrationForm,LoginForm
from django.views.generic import View
from todoapp.models import Todos
from django.contrib.auth import authenticate,login,logout
todos=[

]


# Create your views here.

class TodoCreateView(View):
    template_name="addtodo.html"
    def get(self,request):
        form=TodoForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request):
        form=TodoForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # Todos.objects.create(
            #     task_name=form.cleaned_data.get("task_name"),
            #     user=form.cleaned_data.get("user"),
            #     status=form.cleaned_data.get("status")
            # )
            form.save()
            print("Todo Created")
            return redirect("alltodos")
        else:
            return render(request,self.template_name,{"form":form})

class TodoListView(View):
    def get(self,request):
        all_todos=Todos.objects.all()
        return render(request,"todolist.html",{"todos":all_todos})

class TodoFindView(View):
    template_name="todo_detail.html"
    def get(self,request,*args,**kwargs):
        return render(request,self.template_name)
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        return render(request,self.template_name,{"todo":todo})
        # id=int(request.POST.get("t_id"))
        # todo=[todo for todo in todos if todo["id"]==id][0]
        # return render(request,self.template_name,{"todo":todo})

class TodoDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        return render(request,"details.html",{"todo":todo})

class TodoEditView(View):
    def get_object(self,id):
        return Todos.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=self.get_object(id)
        form=TodoForm(instance=todo)
        return render(request,"todo_edit.html",{"form":form})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=self.get_object(id)
        form=TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("alltodos")
class TodoDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        todo=Todos.objects.get(id=id)
        todo.delete()
        return redirect("alltodos")

class SignUpView(View):
    template_name="register.html"
    def get(self,request,*args,**kwargs):
        form=UserRegistrationForm()
        return render(request,self.template_name,{"form":form})
    def post(self,request,*args,**kwargs):
        form=UserRegistrationForm(request.POST)
        if not form.is_valid():
            return render(request,self.template_name,{"form":form})
        form.save()
        return redirect("signin")

class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                print("login success")
                return redirect("hometodo")
            else:
                print("login failed")
                return redirect("signin")

def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

def home(request,*args,**kwargs):
    return render(request,"home.html")

