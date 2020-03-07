from django import forms
from .models import Tourists

class DateInput(forms.DateInput):
    input_type = 'date'

class TouristsForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    dateOfBirth = forms.DateField(label = 'Date of Birth',widget =DateInput())
    gender = forms.ChoiceField(label='Gender', widget=forms.RadioSelect(), choices=[
                               ('M', 'Male'), ('F', 'Female'), ('O', 'Others')])
    COUNTRIES = [
        ('Nepal', 'Nepal'),
        ('USA', 'USA'),
        ('UK', 'UK'),
        ('Japan', 'Japan'),
        ('China', 'China'),
        ('France', 'France'),
        ('Australia', 'Australia'),
        ('India', 'India'),
        ('Germany', 'Germany'),
    ]
    country = forms.CharField(label='Country', widget=forms.Select(
        attrs={'class': 'form-control'}, choices=COUNTRIES))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    visitType = [
        ('S', 'Sight Seeing'),
        ('B', 'Business'),
        ('T', 'Trekking'),
        ('R', 'Religious')
    ]
    visit_type = forms.CharField(widget=forms.Select(
        attrs={'class': 'form-control'}, choices=visitType))
    arrival_date = forms.DateField(label = 'Arrival Date',widget = DateInput())
    departure_date = forms.DateField(label = 'Departure Date',widget = DateInput())

    class Meta:
        model = Tourists
        # fields = ['first_name','last_name','dateOfBirth','gender','country']
        fields = '__all__'
