import datetime

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from app.forms import BookCreateForm, BokUpdateForm
from app.models import Book


# Create your views here.
class BooksListView(ListView):
    template_name = 'books/list.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        limit = request.GET.get('limit', 2)

        self.paginate_by = limit

        return super().get(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['now'] = datetime.datetime.now()
        context['limit'] = self.paginate_by
        return context


class BookDetailView(DetailView):
    template_name = 'books/detail.html'
    model = Book
    context_object_name = 'book'


class BookCreateView(CreateView):
    template_name = 'books/create.html'
    model = Book
    form_class = BookCreateForm
    success_url = reverse_lazy('list')


class UpdateBookView(UpdateView):
    template_name = 'books/update.html'
    model = Book
    form_class = BokUpdateForm
    success_url = reverse_lazy('list')


class DeleteBookView(DeleteView):
    template_name = 'books/delete.html'
    model = Book
    success_url = reverse_lazy('list')
