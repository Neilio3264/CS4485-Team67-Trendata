from django.db import models
from address.models import AddressField
from datetime import date
import string
import random

def generate_unique_code():
    length = 6
    
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
        
    return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=8, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

GENDER = (('M', 'Male'), ('F', 'Female'))
class Patient(models.Model):
    name = models.CharField(max_length=128, default="", unique=False)
    gender = models.CharField(max_length=1, choices=GENDER)
    location = AddressField(null=True, blank=True)
    dob = models.DateField(default=date.today)
    age = models.PositiveSmallIntegerField(default=0)
    username = models.CharField(max_length=128, default="", unique=True)
    password = models.CharField(max_length=128, default="", unique=False)
    email = models.CharField(max_length=128, default="", unique=False)
    phone = models.CharField(max_length=10, default="", unique=False)
    
    provider = models.CharField(max_length=128, default="", unique=False)
    mri = models.CharField(max_length=128, default="", unique=False)
    aki = models.CharField(max_length=128, default="", unique=False)
    exchange = models.CharField(max_length=128, default="", unique=False)
    