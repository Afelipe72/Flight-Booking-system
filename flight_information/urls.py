from django.urls import path
from flight_information.views import *
urlpatterns = [
    path('', FlightInfoMain.as_view(), name='flight_information_home'),
    path('flight-schedules/', FlightSchedule.as_view(), name='flight_schedule'),
    path('flight-rate/', FlightRate.as_view(), name='flight_rate'),
    path('flight-information', FlightInformation.as_view(), name='flight_information'),
]
