from rest_framework import serializers
from .models import Patient
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'gender', 'location', 'dob', 'age', 'username', 'password', 'email', 'phone', 'provider', 'mri', 'aki', 'exchange')