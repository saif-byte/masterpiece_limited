from django.contrib import admin
from main.models import ToDoList, Customer,Artist,Owner, Painting,HiredPainting
# Register your models here.

admin.site.register(ToDoList)
admin.site.register(Customer)
admin.site.register(Artist)
admin.site.register(Owner)
admin.site.register(Painting)
admin.site.register(HiredPainting)