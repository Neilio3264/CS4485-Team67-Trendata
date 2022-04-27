from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('patient', index),
    path('patient/<str:patientId>', index)
]
