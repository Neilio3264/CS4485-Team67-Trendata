from pyexpat import model
from rest_framework import serializers
from .models import Patient, HealthMetrics, QualityOfLife, Cities
        
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('patient_id', 'first_name', 'last_name', 'age', 'gender', 'phone')

class HealthMetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthMetrics
        fields = ('patient_id', 'Dias_blood_pressure', 'ur_specific_gravity', 'ur_albumin', 'ur_sugar', 'red_blood_cells', 'ur_pus_cell', 'ur_pus_cell_Clumps', 'ur_bacteria', 'blood_glucose_random', 'blood_urea', 'sodium', 'potassium', 'hemoglobin', 'packed_cell_volume', 'white_blood_cell_count', 'red_blood_cell_count', 'hypertension', 'diabetes', 'coronary_artery_disease', 'appetite', 'pedal_edema', 'anemia', 'classification')

class QualityOfLifeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityOfLife
        fields = ('city_id', 'quality_of_life', 'purchase_power', 'healthcare', 'pollution', 'crime')

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ('id', 'city', 'country')