from django.db import models
from django.utils import timezone
from address.models import AddressField

GENDER = (('M', 'male'), ('F', 'female'))
AKI = ((0, 'Stage 0'), (1, 'Stage 1'), (2, 'Stage 2'), (3, 'Stage 3'))
NORM = (('N', 'normal'), ('A', 'abnormal'))
PRES = (('P', 'present'), ('N', 'notpresent'))
ANS = (('Y', 'yes'), ('N', 'no'))
STAT = (('G', 'good'), ('B', 'poor'))
CLASS = (('C', 'ckd'), ('N', 'notckd'))

class Patient(models.Model):
    patient_id = models.PositiveSmallIntegerField(primary_key=True, unique=True)
    first_name = models.CharField(max_length=32, unique=False)
    last_name = models.CharField(max_length=32, unique=False)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER)
    phone = models.CharField(max_length=13, default="(XXX)-XXX-XXXX", unique=True)
    nearest_city = models.PositiveSmallIntegerField()
    city_distance = models.FloatField(default=32000)

class Address(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    location = AddressField(on_delete=models.CASCADE)

class CreatinineHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    inpatient = models.BooleanField()
    creatinine = models.FloatField()
    aki = models.PositiveSmallIntegerField(choices=AKI)

class HealthMetrics(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Dias_blood_pressure = models.FloatField(null=True)
    ur_specific_gravity = models.FloatField(null=True)
    ur_albumin = models.FloatField(null=True)
    ur_sugar = models.FloatField(null=True)
    red_blood_cells = models.CharField(max_length=1, choices=NORM, null=True)
    ur_pus_cell = models.CharField(max_length=1, choices=NORM, null=True)
    ur_pus_cell_Clumps = models.CharField(max_length=1, choices=PRES, null=True)
    ur_bacteria = models.CharField(max_length=1, choices=PRES, null=True)
    blood_glucose_random = models.FloatField(null=True)
    blood_urea = models.FloatField(null=True)
    sodium = models.FloatField(null=True)
    potassium = models.FloatField(null=True)
    hemoglobin = models.FloatField(null=True)
    packed_cell_volume = models.PositiveSmallIntegerField(null=True)
    white_blood_cell_count = models.PositiveSmallIntegerField(null=True)
    red_blood_cell_count = models.FloatField(null=True)
    hypertension = models.CharField(max_length=1, choices=ANS, null=True)
    diabetes = models.CharField(max_length=1, choices=ANS, null=True)
    coronary_artery_disease = models.CharField(max_length=1, choices=ANS, null=True)
    appetite = models.CharField(max_length=1, choices=STAT, null=True)
    pedal_edema = models.CharField(max_length=1, choices=ANS, null=True)
    anemia = models.CharField(max_length=1, choices=ANS, null=True)
    classification = models.CharField(max_length=1, choices=CLASS, null=True)

class Cities(models.Model):
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=13, default='United States')

class QualityOfLife(models.Model):
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)
    quality_of_life = models.FloatField()
    purchase_power = models.FloatField()
    healthcare = models.FloatField()
    pollution = models.FloatField()
    crime = models.FloatField()