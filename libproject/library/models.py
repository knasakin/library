from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField('Book', through='Authored')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField('Author', through='Authored')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Authored(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
