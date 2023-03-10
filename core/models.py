from django.db import models

# Create your models here.

class Country(models.Model):
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.country
    
    class Meta:
        verbose_name = 'olke'
        verbose_name_plural = 'olkeler'



class Author(models.Model):
    name = models.CharField(max_length=300)
    age = models.PositiveIntegerField()
    country  = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=True) # blank=True - true oldugu halda Important deyil
    
    def __str__(self):
        return self.name




class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.genre_name


class Language(models.Model):
    lang_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.lang_name  #representation
    

class Book(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=300)
    price    = models.IntegerField()
    author   = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    genre    = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True, blank=True)
    language = models.ManyToManyField(Language)
    

    def __str__(self):
        return self.title
    


    #   ManyToManyField - olanda  on_delete=models.CASCADE, null=True  - olmur
    #   author   = models.OneToOneField(Author, on_delete=models.CASCADE, null=True, blank=True)   #blank="True" 
    #
    #           Admin                                     DB
    #                                           null=True   - bazada bos saxlamaq olar
    #                                           null=False  - bazada doldurmaq lazimdir
    # blank=True  - required olmur 



