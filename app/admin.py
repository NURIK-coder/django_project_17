from django.contrib import admin

from app.models import Book, Genre

# Register your models here.

admin.site.register(Book)
admin.site.register(Genre)