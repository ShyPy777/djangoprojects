from django.db import models
class Book(models.Model):#Table definition
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    price=models.IntegerField()
    pdf=models.FileField(upload_to='book/pdf')
    cover=models.ImageField(upload_to='book/img',null=True,blank=True)
    def __str__(self):
        return self.title

class Student(models.Model):#Table definition
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    age=models.IntegerField()

    def __str__(self):
        return self.name