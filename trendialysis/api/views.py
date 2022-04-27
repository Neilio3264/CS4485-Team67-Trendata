from rest_framework import generics
from .serializers import PatientSerializer
from .models import Patient


class ViewPatients(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class CreatePatients(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer