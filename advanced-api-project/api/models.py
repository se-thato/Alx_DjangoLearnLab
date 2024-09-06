from django.db import models

class Author(models.Model):
    #creating a model of Author
    name = models.CharField(max_length= 100)

    def __str__(self):
        return self.name

class Book(models.Model):
    #created a model of Book
    title = models.CharField(max_length=100)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name= "book", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
