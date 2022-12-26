from django.db import models

# Create your models here.
class ToDoList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList , on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    complete = models.BooleanField()

    def __str__(self) -> str:
        return self.text

class Customer(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True , unique = True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=10)
    category = models.CharField(max_length=1)

    
    def __str__(self) -> str:
        return self.name

class Artist(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True , unique = True)
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    year_of_birth = models.PositiveSmallIntegerField()
    year_of_death  = models.PositiveSmallIntegerField(null=True)

    def __str__(self) -> str:
        return self.name

