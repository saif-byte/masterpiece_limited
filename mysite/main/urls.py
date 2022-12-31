from django.urls import  path
from main import views

urlpatterns = [
    #path("<int:id>" , views.index , name="index"),
    
    #path("create" , views.create  , name = "create"),
    path("create-customer" , views.create_customer  , name = "create-customer"),
    path("customers/<int:id>" , views.customer_index , name="cust_index"),
    path("create-artist" , views.create_artist  , name = "create-customer"),
    path("artists/<int:id>" , views.artist_index , name="cust_index"),
    path("create-owner" , views.create_owner  , name = "create-owner"),
    path("owners/<int:id>" , views.owner_index , name="owner_index"),
    path("create-painting" , views.create_painting  , name = "create-painting"),
    path("paintings/<int:id>" , views.painting_index , name="painting_index"),
    path("paintings" , views.all_paintings , name="all_paintings"),
    path("hire-painting" , views.hire_painting , name="hire_painting"),
    path("hired/<int:id>" , views.hire_index , name="hire_index"),
    path("return-painting" , views.return_painting , name="return_painting"),
    path("gen-cust-rent-rpt" , views.gen_cust_rent_rpt , name="gen_cust_rent_rpt"),
    path("customer-rental-report/<int:id>" , views.customer_rental_report , name="customer-rental-rpt"),
    path("gen-artist-rpt" , views.gen_artist_rpt , name="gen_artist_rpt"),
    path("artist-report/<int:id>" , views.artist_report , name="artist_report"),
    path("gen-owner-rpt" , views.gen_owner_rpt , name="gen_owner_rpt"),
    path("owner-report/<int:id>" , views.owner_report , name="owner_report"),
    path("monthly-update" , views.monthly ,name="monthly" ),
    path("customers" , views.customers ,name="customers" ),
    path("artists" , views.artists ,name="artists" ),
    path("owners" , views.owners ,name="owners" ),
    path("" , views.home , name = "home"),

]

