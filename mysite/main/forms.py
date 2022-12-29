from django import forms
from django.core.validators import MinLengthValidator , MaxLengthValidator
from main.constants import COUNTRIES, THEMES
from mysite import settings
import datetime

date_today = datetime.datetime.now()
date_today = date_today.strftime("%d/%m/%Y")


class createNewList(forms.Form):
    name = forms.CharField(label="Name" , max_length=200)

class createNewCustomer(forms.Form):
    id = forms.CharField(label = "id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    name =  forms.CharField(label="name" , max_length=200)
    address = forms.CharField(label = "address" , max_length=200)
    city = forms.CharField(label = "city" , max_length=10)
    category = forms.ChoiceField(label='Category', choices=[("B", "B"), ("S", "S"), ("G", "G"), ("P", "P")])

class createNewArtist(forms.Form):
    id = forms.CharField(label = "id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    name = forms.CharField(label="name" , max_length=200)
    country = forms.ChoiceField(label = "country" , choices=COUNTRIES)
    year_of_birth = forms.CharField(label = "year_of_birth" , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    year_of_death = forms.CharField(label = "year_of_death" , required = False , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])

class createNewOwner(forms.Form):
    id = forms.CharField(label = "id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    name = forms.CharField(label="name" , max_length=200)
    address = forms.CharField(label = "address" , max_length=200)
    city = forms.CharField(label = "city" , max_length=10)

class createNewPainting(forms.Form):
    id = forms.CharField(label = "id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    title = forms.CharField(label="title" , max_length=200)
    theme = forms.ChoiceField(label="theme" , choices=THEMES)
    rent = forms.FloatField(label="rent")
    owner_id = forms.CharField(label = "owner_id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    artist_id = forms.CharField(label = "artist_id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    
class hirePainting(forms.Form):
    customer_id = forms.CharField(label = "customer_id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    painting_id = forms.CharField(label = "painting_id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    hire_date = forms.DateField(label = "hire_date" , input_formats = settings.DATE_INPUT_FORMATS , initial=date_today)
    due_date = forms.DateField(label = "due_date" , input_formats = settings.DATE_INPUT_FORMATS)

class returnPainting(forms.Form):
    customer_id = forms.CharField(label = "customer_id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
    painting_id = forms.CharField(label = "painting_id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
   
class cust_rpt(forms.Form):
    id = forms.CharField(label = "id" , required =True , validators=[
        MinLengthValidator(4) , MaxLengthValidator(4)])
        