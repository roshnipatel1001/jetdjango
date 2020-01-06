from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    DOB = models.DateField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=255)
    Author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    publition_date = models.DateField()