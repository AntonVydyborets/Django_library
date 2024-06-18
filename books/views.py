from django.shortcuts import render, get_object_or_404, redirect
from books.models import Book, Genre, Author
from books.forms import BookForm

# Create your views here.
def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'authors/authors_list.html', context)

def books_list(request):
    books = Book.objects.all()
    genres = Genre.objects.all()
    context = {
        'books': books,
        'genres': genres,
    }
    return render(request, 'books/books_list.html', context)

def genre_detail(request, genre_id):
    books = Book.objects.filter(genre__id=genre_id)
    genres = Genre.objects.all()
    genre = Genre.objects.get(pk=genre_id)
    context = {
        'books': books,
        'genres': genres,
        'genre': genre
    }
    return render(request, 'books/genre.html', context)  

def book_detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    context = {
        'book': book,

    }
    return render(request, 'books/genre.html', context)  

def add_book(request):
    if request.method == 'POST':
         form = BookForm(request.POST, request.FILES)
         if form.is_valid():
            book = Book.objects.create(**form.cleaned_data)
            return redirect('book_detail', book_id=book.pk)
    else:
        form = BookForm()
        return render(request, 'books/create_book2.html', {'form': form})