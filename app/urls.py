from django.urls import path

from app.views import BooksListView, BookDetailView, BookCreateView, UpdateBookView, DeleteBookView

urlpatterns = [
    path('list/', BooksListView.as_view(), name='list'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('create/', BookCreateView.as_view(), name='create'),
    path('update/<int:pk>', UpdateBookView.as_view(), name='update'),
    path('delete/<int:pk>', DeleteBookView.as_view(), name='delete')
]