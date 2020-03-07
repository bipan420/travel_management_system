from django.db import models
from django.contrib.auth.models import User

class Abs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dateOfBirth = models.DateField(auto_now = False,null=True,blank=True)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    visit_type = models.CharField(max_length=50)
    arrival_date = models.DateField(auto_now=True,null=True,blank=True)
    departure_date = models.DateField(auto_now=False,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True