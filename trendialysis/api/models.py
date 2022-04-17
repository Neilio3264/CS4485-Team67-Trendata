from django.db import models
from address.models import AddressField
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
    
class Patient(models.Model):
    GENDER = (('M', 'Male'),
              ('F', 'Female'),
              )
    
    name = models.CharField(max_length=128, default="", unique=False)
    gender = models.CharField(max_length='1', choices=GENDER)
    location = AddressField()
    