from django.db import models
from mysite import settings

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

class Owner(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True , unique = True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return self.name


class Painting(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True , unique = True)
    title =  models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    rent = models.FloatField()
    owner_id = models.ForeignKey(Owner , on_delete=models.CASCADE )
    artist_id = models.ForeignKey(Artist , on_delete=models.CASCADE )
    mth_to_rtn = models.PositiveSmallIntegerField(default = 6) 
    rtn_to_owner = models.BooleanField(default=False)
    hired = models.BooleanField(default=False)
    submit_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    def __str__(self) -> str:
        return self.title

class HiredPainting(models.Model):
    customer_id = models.ForeignKey(Customer , on_delete=models.CASCADE)
    painting_id = models.ForeignKey(Painting , on_delete=models.CASCADE)
    hired_date = models.DateField()
    due_date = models.DateField()
    returned = models.BooleanField(default=False)
    appl_rent = models.FloatField()