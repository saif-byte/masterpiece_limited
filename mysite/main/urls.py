from django.urls import  path
from main import views

urlpatterns = [
    #path("<int:id>" , views.index , name="index"),
    
    #path("create" , views.create  , name = "create"),
    path("create-customer" , views.create_customer  , name = "create-customer"),
    path("customers/<int:id>" , views.customer_index , name="cust_index"),
    path("create-artist" , views.create_artist  , name = "create-customer"),
    path("artists/<int:id>" , views.artist_index , name="cust_index"),
    path("" , views.home , name = "home"),

]

