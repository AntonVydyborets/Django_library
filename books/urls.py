from django.urls import path
from .views import books_list, genre_detail, author_list, book_detail,add_book


urlpatterns = [
    path('', books_list, name='books_list'),
    path('book/<int:book_id>', book_detail, name='books_detail'),
    path('genre/<int:genre_id>', genre_detail, name='genre_detail'),
    path('authors', author_list, name='author_list'),
    path('books/add-book', add_book, name='add_book'),
]
