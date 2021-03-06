from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from books_cbv.models import Book

class BookList(ListView):
    model = Book

class BookCreate(CreateView):
    model = Book
    success_url = reverse_lazy('books_cbv:book_list')

class BookUpdate(UpdateView):
    model = Book
    success_url = reverse_lazy('books_cbv:book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('books_cbv:book_list')