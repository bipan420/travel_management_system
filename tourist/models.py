from django.db import models
from abstract.models import Abs

# Create your models here.




class Tourists(Abs):
    class Meta:
        db_table = 'tourists'

    def __str__(self):
        return self.first_name
    