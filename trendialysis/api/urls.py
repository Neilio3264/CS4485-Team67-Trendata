from django.urls import path
from .views import ViewPatients, CreatePatients, GetPatient, GetPatients, GetMetrics, GetQuality, GetCity

urlpatterns = [
    path('view/', ViewPatients.as_view()),
    path('create/', CreatePatients.as_view()),
    path('get-patient', GetPatient.as_view()),
    path('get-patients', GetPatients.as_view()),
    path('get-metrics', GetMetrics.as_view()),
    path('get-quality', GetQuality.as_view()),
    path('get-city', GetCity.as_view())
]
