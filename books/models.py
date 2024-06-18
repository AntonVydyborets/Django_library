from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to="books/profile_images", null=True, blank=True)

    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):

        return f'{self.first_name} {self.last_name}'

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    cover_image = models.ImageField(upload_to='books/images/', null=True, blank=True)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=True)
    genre = models.ForeignKey('Genre', on_delete=models.PROTECT, null=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):

        return f'{self.title}/{self.author}'
    
    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['title']

class Genre(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name="Genre")

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
    
    def __str__(self):

        return f'{self.title}'