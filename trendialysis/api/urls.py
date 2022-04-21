from django.urls import path
from .views import RoomView, ViewPatients, CreatePatients

urlpatterns = [
    path('', RoomView.as_view()),
    path('view/', ViewPatients.as_view()),
    path('create/', CreatePatients.as_view())
]
