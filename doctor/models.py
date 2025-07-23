from django.db import models
from user.models import CustomUser 
from django.contrib.auth.decorators import login_required
from pharmacy.models import Prescription

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    hospital = models.CharField(max_length=100)
    experience = models.IntegerField()
    is_available = models.BooleanField(default=True)
    fee = models.DecimalField(max_digits=6, decimal_places=2,default=500)
    rating = models.FloatField()
    address= models.TextField(default='Not Provided')
 

    def __str__(self):
        return self.name

