from rest_framework import serializers
from .models import Room, Patient

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'name', 'gender', 'location', 'dob', 'age', 'username', 'password', 'email', 'phone', 'provider', 'mri', 'aki', 'exchange')