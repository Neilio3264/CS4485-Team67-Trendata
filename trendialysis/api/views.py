from rest_framework import generics
from .serializers import RoomSerializer, PatientSerializer
from .models import Room, Patient

# Create your views here.
class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ViewPatients(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class CreatePatients(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer