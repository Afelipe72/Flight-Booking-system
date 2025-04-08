from django.urls import path
from flight_reservation.views import *
urlpatterns = [
    path('', ticket_reservation, name='flight_reservation'),
]
