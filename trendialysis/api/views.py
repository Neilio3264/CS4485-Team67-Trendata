from rest_framework import generics, status
from .serializers import PatientSerializer, HealthMetricsSerializer, QualityOfLifeSerializer, CitySerializer
from .models import Patient, HealthMetrics, QualityOfLife, Cities
from rest_framework.views import APIView
from rest_framework.response import Response

class ViewPatients(generics.ListAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class GetPatients(APIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    
    def get(self, format=None):
        patients = Patient.objects.all()
        if len(patients) > 0:
            return Response(PatientSerializer(patients, many=True).data, status=status.HTTP_200_OK)
        return Response({'Patients Not Found': 'Patient Objects cannot be returned'}, status=status.HTTP_404_NOT_FOUND)

class GetPatient(APIView):
    serializer_class = PatientSerializer
    lookup_url_kwarg = 'patient_id'
    
    def get(self, request, format=None):
        patient_id = request.GET.get(self.lookup_url_kwarg)
        if patient_id != None:
            patient = Patient.objects.filter(patient_id=patient_id)
            if len(patient) > 0:
                return Response(PatientSerializer(patient[0]).data, status=status.HTTP_200_OK)
            return Response({'Patient Not Found': 'Invalid Patient ID'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'PatientId parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)

class GetMetrics(APIView):
    serializer_class = HealthMetricsSerializer
    lookup_url_kwarg = 'patient_id'
    
    def get(self, request, format=None):
        patient_id = request.GET.get(self.lookup_url_kwarg)
        if patient_id != None:
            patient = HealthMetrics.objects.filter(patient_id=patient_id)
            if len(patient) > 0:
                return Response(HealthMetricsSerializer(patient[0]).data, status=status.HTTP_200_OK)
            return Response({'Patient Not Found': 'Invalid Patient ID'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'PatientId parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)

class GetQuality(APIView):
    serializer_class = QualityOfLifeSerializer
    lookup_url_kwarg = 'city_id'
    
    def get(self, request, format=None):
        city_id = request.GET.get(self.lookup_url_kwarg)
        if city_id != None:
            city = QualityOfLife.objects.filter(city_id=city_id)
            if len(city) > 0:
                return Response(QualityOfLifeSerializer(city[0]).data, status=status.HTTP_200_OK)
            return Response({'City Not Found': 'Invalid City ID'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'CityId parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)

class GetCity(APIView):
    serializer_class = CitySerializer
    lookup_url_kwarg = 'city_id'
    
    def get(self, request, format=None):
        city_id = request.GET.get(self.lookup_url_kwarg)
        if city_id != None:
            city = Cities.objects.filter(id=city_id)
            if len(city) > 0:
                return Response(CitySerializer(city[0]).data, status=status.HTTP_200_OK)
            return Response({'City Not Found': 'Invalid City ID'}, status=status.HTTP_404_NOT_FOUND)
        
        return Response({'Bad Request': 'CityId parameter not found in request'}, status=status.HTTP_400_BAD_REQUEST)

class CreatePatients(generics.CreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer