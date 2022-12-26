from django.contrib import admin
from main.models import ToDoList, Customer,Artist
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Customer)
admin.site.register(Artist)