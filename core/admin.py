from django.contrib import admin

from core.models import Author, Book, Country, Genre, Language

# Register your models here.

admin.site.register([Author, Book, Genre, Language,Country])