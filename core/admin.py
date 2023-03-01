from django.contrib import admin

from core.models import Author, Book, Genre, Language

# Register your models here.

admin.site.register([Author, Book, Genre, Language])