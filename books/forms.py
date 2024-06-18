from books.models import Book
from django.forms import ModelForm

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cover_image', 'description', 'publication_date', 'author', 'genre']