from django.urls import path
from todoapp import views


urlpatterns=[
    path("add",views.TodoCreateView.as_view(),name="addtodo"),
    path("all",views.TodoListView.as_view(),name="alltodos"),
    path("find",views.TodoFindView.as_view(),name="findtodo"),
    path("details/<int:id>",views.TodoDetailView.as_view(),name="details"),
    path("change/<int:id>",views.TodoEditView.as_view(),name="changetodo"),
    path("remove/<int:id>",views.TodoDeleteView.as_view(),name="removetodo"),
    path("accounts/signup",views.SignUpView.as_view(),name="signup")
]