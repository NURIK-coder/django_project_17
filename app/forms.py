from django import forms

from app.models import Book


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'year', 'genres']


class BokUpdateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'year', 'genres']