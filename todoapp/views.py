from django.shortcuts import render,redirect
from todoapp.forms import TodoForm,UserRegistrationForm,LoginForm
from django.views.generic import View,ListView,DetailView,UpdateView
from django.urls import reverse_lazy
from todoapp.models import Todos
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator
from todoapp.decorators import sigin_required
todos=[

]


# Create your views here.

@method_decorator(sigin_required,name="dispatch")
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
            form.instance.user=request.user
            form.save()
            print("Todo Created")
            return redirect("alltodos")
        else:
            return render(request,self.template_name,{"form":form})

@method_decorator(sigin_required,name="dispatch")
class TodoListView(ListView):
    # def get(self,request):
    #     all_todos=Todos.objects.filter(user=request.user)
    #     return render(request,"todolist.html",{"todos":all_todos})
    model = Todos
    template_name = "todolist.html"
    context_object_name = "todos"
    def get_queryset(self):
        return Todos.objects.filter(user=self.request.user)

@method_decorator(sigin_required,name="dispatch")
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

@method_decorator(sigin_required,name="dispatch")
class TodoDetailView(DetailView):
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=Todos.objects.get(id=id)
    #     return render(request,"details.html",{"todo":todo})
    model = Todos
    template_name = "details.html"
    context_object_name = "todo"
    pk_url_kwarg = "id"

@method_decorator(sigin_required,name="dispatch")
class TodoEditView(UpdateView):
    model = Todos
    template_name = "todo_edit.html"
    form_class = TodoForm
    success_url = reverse_lazy("alltodos")
    pk_url_kwarg = "id"
    # def get_object(self,id):
    #     return Todos.objects.get(id=id)
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=self.get_object(id)
    #     form=TodoForm(instance=todo)
    #     return render(request,"todo_edit.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get("id")
    #     todo=self.get_object(id)
    #     form=TodoForm(request.POST,instance=todo)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("alltodos")

@method_decorator(sigin_required,name="dispatch")
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

@sigin_required
def signout(request,*args,**kwargs):
    logout(request)
    return redirect("signin")

@sigin_required
def home(request,*args,**kwargs):
    return render(request,"home.html")

