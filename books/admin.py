from django.contrib import admin
from books.models import Author, Book, Genre
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
