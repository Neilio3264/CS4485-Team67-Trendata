from django.urls import path
from .views import ViewPatients, CreatePatients, GetPatient, GetPatients

urlpatterns = [
    path('view/', ViewPatients.as_view()),
    path('create/', CreatePatients.as_view()),
    path('get-patient', GetPatient.as_view()),
    path('get-patients', GetPatients.as_view())
]
