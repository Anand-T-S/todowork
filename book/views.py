from django.shortcuts import render,redirect
from book.forms import BookForm
from book.models import Books
from django.views.generic import CreateView,ListView,DetailView,UpdateView
from django.urls import reverse_lazy
# Create your views here.

class BookCreateView(CreateView):
    model = Books
    form_class = BookForm
    template_name = "book-add.html"
    success_url = reverse_lazy("book-list")


class BookListView(ListView):
    model = Books
    template_name = "book-list.html"
    context_object_name = "books"    #key to override predefine


class BookDetailView(DetailView):
    model = Books
    template_name = "book-detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"  #to pass id with url


class BookEditView(UpdateView):
    model = Books
    form_class = BookForm
    template_name = "book-edit.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("book-list")

def bookdelete(request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    return redirect("book-list")






