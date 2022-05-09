from django.urls import path
from book import views

urlpatterns = [
    path("add", views.BookCreateView.as_view(), name="book-add"),
    path("list", views.BookListView.as_view(), name="book-list"),
    path("detail/<int:id>", views.BookDetailView.as_view(), name="book-detail"),
    path("change/<int:id>", views.BookEditView.as_view(), name="book-change"),
    path("remove/<int:id>",views.bookdelete,name="book-delete"),
]
