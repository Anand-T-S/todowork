from django.urls import path
from todoapp import views


urlpatterns=[
    path("add",views.TodoCreateView.as_view(),name="addtodo"),
    path("all",views.TodoListView.as_view(),name="alltodos"),
]