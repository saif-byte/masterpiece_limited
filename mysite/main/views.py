from django.shortcuts import render
from django.db import IntegrityError
from django.db import connection
from django.http import HttpResponse,HttpResponseRedirect 
from main.models import ToDoList, Item , Customer ,Artist, Owner,Painting ,HiredPainting
from main.forms import createNewList , createNewCustomer ,createNewArtist,createNewOwner , createNewPainting,hirePainting,returnPainting,cust_rpt
from main.db_utils import all_painting_view ,trigger_on_hiredpainting,make_is_hired_func,rtn_pnt,cal_rent,get_disc , get_date_sixmth,sub_rtn_date,rtndate_when_hired_trig,is_return_to_owner,monthly_update
from dateutil.relativedelta import relativedelta
import datetime
# Create your views here.

def dictfetchall(cursor): 
    "Returns all rows from a cursor as a dict" 
    desc = cursor.description 
    return [
            dict(zip([col[0] for col in desc], row)) 
            for row in cursor.fetchall() 
    ]

v = all_painting_view()
trigger_on_hiredpainting()
make_is_hired_func()
rtn_pnt()
cal_rent()
get_disc()
get_date_sixmth()
sub_rtn_date()
rtndate_when_hired_trig()
is_return_to_owner()
monthly_update()

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
                if str(yod)!='' and yob>yod:
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


def create_owner(response):
    if response.method == "POST":
        owner_form = createNewOwner(response.POST)
        if owner_form.is_valid():
            i = owner_form.cleaned_data["id"]
            n = owner_form.cleaned_data["name"]
            add = owner_form.cleaned_data["address"]
            cty = owner_form.cleaned_data["city"]
            answers = Owner.objects.filter(id=i)
            if not answers:
                with connection.cursor() as cursor:
                    r = cursor.execute(
                        f"INSERT INTO main_owner VALUES ({i} ,'{n}' , '{add}' , '{cty}');")
                    return HttpResponseRedirect("owners/%s" %i)
            else:
                error = "Owner with ID already exists !"
                return render(response , "main/error.html" , {"error" : error} )
            
        else:
            return render(response , "main/create-owner.html" , {"form" : owner_form})
    else:  
        owner_form = createNewOwner()
        return render(response , "main/create-owner.html" , {"form" : owner_form})


def owner_index(response, id):
   
    owner = Owner.objects.get(id = id)
    return render(response , "main/display_owner_det.html" , {"owner":owner})


def create_painting(response):
    if response.method == "POST":
        painting_form = createNewPainting(response.POST)
        if painting_form.is_valid():
            i = painting_form.cleaned_data["id"]
            ttl = painting_form.cleaned_data["title"]
            thm = painting_form.cleaned_data["theme"]
            rent = painting_form.cleaned_data["rent"]
            own_id= int(painting_form.cleaned_data["owner_id"])
            art_id= int(painting_form.cleaned_data["artist_id"])
            answers = Painting.objects.filter(id=i)
            own_exist = Owner.objects.filter(id=own_id)
            art_exist  = Artist.objects.filter(id=art_id)
            if not answers:
                if not own_exist:
                    error = "Owner does not exist, please create owner."
                    return render(response , "main/error.html" , {"error" : error} )
                elif not art_exist:
                    error = "Artist does not exist, please create artist."
                    return render(response , "main/error.html" , {"error" : error} )
                with connection.cursor() as cursor:
                        r = cursor.execute(
                            f'''INSERT INTO main_painting(id,title,theme,rent,owner_id_id,artist_id_id,mth_to_rtn,rtn_to_owner,hired) 
                             VALUES ({i} ,'{ttl}' , '{thm}' , {rent} , {own_id} , {art_id} , 6 , 0, 0);''')
                        cursor.callproc("sub_rtn_date" , [i])     
                        return HttpResponseRedirect("paintings/%s" %i)
            else:
                error = "Painting with ID already exists !"
                return render(response , "main/error.html" , {"error" : error} )
            
        else:
            return render(response , "main/create-painting.html" , {"form" : painting_form})
    else:  
        painting_form = createNewPainting()
        return render(response , "main/create-painting.html" , {"form" : painting_form})


def painting_index(response, id):
   
    painting = Painting.objects.get(id = id)
    return render(response , "main/display_painting_det.html" , {"painting":painting})


def all_paintings(response):
    with connection.cursor() as cursor:
        #allpaintings is a view created in db_utils
        cursor.execute('SELECT * FROM allpaintings;')
        results = dictfetchall(cursor = cursor)
        return render(response , "main/paintings.html" , {"results":results})

def hire_painting(response):
    cursor = connection.cursor()
    if response.method == "POST":
        hire_form = hirePainting(response.POST)
        
        
        if hire_form.is_valid():
            c_id = hire_form.cleaned_data["customer_id"]
            p_id = hire_form.cleaned_data["painting_id"]
            h_date = hire_form.cleaned_data["hire_date"]
            d_date = hire_form.cleaned_data["due_date"]
            cust_exist = Customer.objects.filter(id = c_id)
            paint_id = Painting.objects.filter(id = p_id)
            if not cust_exist: 
                error = "Customer do not exist"
                return render(response , "main/error.html" , {"error" : error} )
            if not paint_id: 
                error = "Painting do not exist"
                return render(response , "main/error.html" , {"error" : error} )
            if h_date > d_date:
                error = "Due date cannot be less than Hire date"
                return render(response , "main/error.html" , {"error" : error} )
            with connection.cursor() as cursor:
                is_hired = cursor.callfunc("is_hired" , int , [p_id])
                is_return_to_owner = cursor.callfunc("is_return_to_owner" , int , [p_id])
                if not is_hired and not is_return_to_owner:
                    try:
                        app_rent = cursor.callfunc('cal_rent' ,int , [c_id , p_id])
                        r = cursor.execute(
                            f'''INSERT INTO main_hiredpainting (customer_id_id , painting_id_id , hired_date , due_date , returned , appl_rent)
                            VALUES ({c_id},{p_id},'{h_date}' , '{d_date}' , 0 , {app_rent} );''')
                        return HttpResponseRedirect("hired/%s" %c_id)
                    except IntegrityError as e:
                        return render(response , "main/error.html" , {"error" : e} )
                else:
                    error = "The painting is already hired or the painting is returned to owner"
                    return render(response , "main/error.html" , {"error" : error} )
        else:
            return render(response , "main/hire-painting.html" , {"form" : hire_form})
    else:  
        hire_form = hirePainting()
        return render(response , "main/hire-painting.html" , {"form" : hire_form})

def hire_index(response , id):
    cursor = connection.cursor()
    cursor.execute(f'''select * from main_hiredpainting where customer_id_id={id};''')
    hire = dictfetchall(cursor = cursor)
    return render(response , "main/display-hire-det.html" , {"hire":hire , "cust_id" : id})


def return_painting(response):
    cursor = connection.cursor()
    if response.method == "POST":
        ret_form = returnPainting(response.POST)
        
        if ret_form.is_valid():
            c_id = ret_form.cleaned_data["customer_id"]
            p_id = ret_form.cleaned_data["painting_id"]
            with connection.cursor() as cursor:
                cursor.callproc("rtn_pnt" , [c_id , p_id])
                return HttpResponseRedirect("hired/%s" %c_id)
        else:
            return render(response , "main/return-painting.html" , {"form" : ret_form})
    else:  
        ret_form = returnPainting()
        return render(response , "main/return-painting.html" , {"form" : ret_form})


def gen_cust_rent_rpt(response):
    if response.method == "POST":
        rpt_form = cust_rpt(response.POST)
        
        if rpt_form.is_valid():
            c_id = rpt_form.cleaned_data["id"]
            return HttpResponseRedirect("customer-rental-report/%s" %c_id)
        else:
            return render(response , "main/gen-cust-rent-rpt.html" , {"form" : ret_form})
    else:  
        ret_form = cust_rpt()
        return render(response , "main/gen-cust-rent-rpt.html" , {"form" : ret_form})

def customer_rental_report(response , id):
    paintings = []
    if HiredPainting.objects.filter(customer_id_id = id):
        cursor = connection.cursor()
        cursor.execute(f"select * from main_customer where id =  {id}")
        cust = dictfetchall(cursor)
        disc = cursor.callfunc('get_disc' , int , [id])
        cursor.execute(f"select * from main_hiredpainting where customer_id_id =  {id}")
        painting_ids = dictfetchall(cursor)
        cursor.execute(f'''select main_painting.id , main_painting.title , main_painting.theme , main_hiredpainting.hired_date , main_hiredpainting.due_date, main_hiredpainting.returned FROM main_painting INNER JOIN main_hiredpainting ON main_painting.id = main_hiredpainting.painting_id_id where main_hiredpainting.customer_id_id = {id}''')
        painting_info = dictfetchall(cursor)
        for painting in painting_ids:
            cursor.execute(f"select * from main_painting where id =  {painting['PAINTING_ID_ID']} ;")
            paintings.append(dictfetchall(cursor))

        return render(response , "main/customer-rental-report.html" , {"painting_info": painting_info, "cust" : cust , "painting_ids" : painting_ids , "paintings": paintings , "disc" : disc})
    else:
        error = "This Customer has not hired any painting"
        return render(response , "main/error.html" , {"error" : error} )    

def gen_artist_rpt(response):
    if response.method == "POST":
        rpt_form = cust_rpt(response.POST)
        
        if rpt_form.is_valid():
            c_id = rpt_form.cleaned_data["id"]
            return HttpResponseRedirect("artist-report/%s" %c_id)
        else:
            return render(response , "main/gen-artist-rpt.html" , {"form" : ret_form})
    else:  
        ret_form = cust_rpt()
        return render(response , "main/gen-artist-rpt.html" , {"form" : ret_form})

def artist_report(response , id):
    if Artist.objects.filter(id = id):
        cursor = connection.cursor()
        cursor.execute(f'select * from main_artist where id = {id};')
        artist = dictfetchall(cursor)
        cursor.execute(f'select main_painting.ID as painting_id, main_painting.TITLE as painting_title , main_painting.THEME as painting_theme , main_painting.RENT as painting_rent , main_owner.ID as owner_id , main_owner.NAME as owner_name   from  main_painting INNER JOIN main_artist ON  main_painting.id = main_artist.id INNER JOIN main_owner ON  main_painting.id = main_owner.id  where main_artist.id = {id};')
        painting_info = dictfetchall(cursor)
        return render(response , "main/artist-report.html" , {"artist" : artist , "painting_info" : painting_info})
    else:
        error = "This Artist does not exist"
        return render(response , "main/error.html" , {"error" : error} )    

def gen_owner_rpt(response):
    if response.method == "POST":
        rpt_form = cust_rpt(response.POST)
        
        if rpt_form.is_valid():
            c_id = rpt_form.cleaned_data["id"]
            return HttpResponseRedirect("owner-report/%s" %c_id)
        else:
            return render(response , "main/gen-owner-rpt.html" , {"form" : ret_form})
    else:  
        ret_form = cust_rpt()
        return render(response , "main/gen-owner-rpt.html" , {"form" : ret_form})

def owner_report(response , id):
    if Owner.objects.filter(id = id):
        cursor = connection.cursor()
        cursor.execute(f'select * from main_owner where id = {id};')
        owner = dictfetchall(cursor)
        cursor.execute(f'select main_painting.ID as painting_id, main_painting.TITLE as painting_title , main_painting.RETURN_DATE as painting_return_date from  main_painting INNER JOIN main_owner ON  main_painting.owner_id_id = main_owner.id where main_owner.id = {id};')
        painting_info = dictfetchall(cursor)
        return render(response , "main/owner-report.html" , {"owner" : owner , "painting_info" : painting_info})
    else:
        error = "This Owner does not exist"
        return render(response , "main/error.html" , {"error" : error} )    

def monthly(response):
    cursor = connection.cursor()
    cursor.callproc('monthly_update')

    return render(response , "main/monthly.html")    

def customers(response):
    cursor = connection.cursor()
    cursor.execute('select * from main_customer;')
    customers = dictfetchall(cursor)
    return render(response , "main/customers.html" , {"customers":customers})    
    
def artists(response):
    cursor = connection.cursor()
    cursor.execute('select * from main_artist;')
    artists = dictfetchall(cursor)
    return render(response , "main/artists.html" , {"artists":artists})    

def owners(response):
    cursor = connection.cursor()
    cursor.execute('select * from main_owner;')
    owners = dictfetchall(cursor)
    return render(response , "main/owners.html" , {"owners":owners})    
