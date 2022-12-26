from django import forms
from django.core.validators import MinLengthValidator , MaxLengthValidator
from main.constants import COUNTRIES


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
    