from django.urls import path
from .views import ViewPatients, CreatePatients

urlpatterns = [
    path('view/', ViewPatients.as_view()),
    path('create/', CreatePatients.as_view())
]
