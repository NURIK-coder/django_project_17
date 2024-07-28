from django.db import models as m


# Create your models here.


class Genre(m.Model):
    name = m.CharField('Name', max_length=50)

    def __str__(self):
        return self.name


class Book(m.Model):
    name = m.CharField('Name', max_length=50)
    year = m.IntegerField("Year")
    created_at = m.DateTimeField("Created at", auto_now_add=True)
    genres = m.ManyToManyField(Genre)

    def __str__(self):
        return self.name
