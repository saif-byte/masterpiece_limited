from django.shortcuts import render
from django.db import IntegrityError
from django.db import connection
from django.http import HttpResponse,HttpResponseRedirect 
from main.models import ToDoList, Item , Customer ,Artist
from main.forms import createNewList , createNewCustomer ,createNewArtist
# Create your views here.

'''def index(response , id):
    ls = ToDoList.objects.get(id=id)
    return render(response , "main/list.html" ,{"ls":ls})
'''
def home(response):
    return render(response , "main/home.html")
'''
def create(response):
    if response.method == "POST":
        form = createNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name = n)
            t.save()
            return HttpResponseRedirect("%i" %t.id)
    else:  
        form = createNewList()
    return render(response , "main/create.html" , {"form" : form})'''

def create_customer(response):
    if response.method == "POST":
        cust_form = createNewCustomer(response.POST)
        if cust_form.is_valid():
            i = cust_form.cleaned_data["id"]
            n = cust_form.cleaned_data["name"]
            cat = str(cust_form.cleaned_data["category"])
            add = cust_form.cleaned_data["address"]
            cty = cust_form.cleaned_data["city"]
            answers = Customer.objects.filter(id=i)
            if not answers:
                with connection.cursor() as cursor:
                    r = cursor.execute(
                        f"INSERT INTO main_customer VALUES ({i} ,'{n}' , '{add}' , '{cty}' , '{cat}');")
                    return HttpResponseRedirect("customers/%s" %i)
            else:
                error = "Customer with ID already exists !"
                return render(response , "main/error.html" , {"error" : error} )
            
        else:
            return render(response , "main/create-customer.html" , {"form" : cust_form})
    else:  
        cust_form = createNewCustomer()
        return render(response , "main/create-customer.html" , {"form" : cust_form})


def customer_index(response, id):
   
    cust = Customer.objects.get(id = id)
    return render(response , "main/display_cust_det.html" , {"cust":cust})



def create_artist(response):
    if response.method == "POST":
        art_form = createNewArtist(response.POST)
        if art_form.is_valid():
            i = art_form.cleaned_data["id"]
            n = art_form.cleaned_data["name"]
            cnty = (art_form.cleaned_data["country"]).upper()
            yob = art_form.cleaned_data["year_of_birth"]
            yod = art_form.cleaned_data["year_of_death"]
            answers = Artist.objects.filter(id=i)
            if not answers:
                if yod!=None and yob>yod:
                    error = "Year of Birth cannot be greater than Year of Death"
                    return render(response , "main/error.html" , {"error" : error} )
                with connection.cursor() as cursor:
                    r = cursor.execute(
                        f"INSERT INTO main_artist VALUES ({i} ,'{n}' , '{cnty}' , '{yob}' , '{yod}');")
                    return HttpResponseRedirect("artists/%s" %i)
            else:
                error = "Artist with ID already exists !"
                return render(response , "main/error.html" , {"error" : error} )
            
        else:
            return render(response , "main/create-artist.html" , {"form" : art_form})
    else:  
        art_form = createNewArtist()
        return render(response , "main/create-artist.html" , {"form" : art_form})


def artist_index(response, id):
   
    art = Artist.objects.get(id = id)
    return render(response , "main/display_art_det.html" , {"art":art})
