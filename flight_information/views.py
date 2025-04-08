from django.shortcuts import render
from flight_information.models import *
from buy_tickets.models import TicketPrice
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic import ListView

# flight information landing page
class FlightInfoMain(TemplateView):
    template_name = "flight_information/home.html"

class FlightSchedule(ListView):
    model = flight_schedule  # Automatically fetches all Flight objects
    template_name = "flight_information/flight_schedule.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        flight_info = flight_information.objects.all()
        schedule = flight_schedule.objects.all()
        # get the fields from the departure and destination based on the names
        departure = self.request.GET.get("Departure", "")
        destination = self.request.GET.get("Destination", "")
        # checks the filter for a departure flight
        if departure and departure != 'Any':    
            # get all the records for table "flight_information" where the origin airport matches
            flight_info = flight_info.filter(origin_airport__airport_country=departure)
        if destination and destination != 'Any':
            flight_info = flight_info.filter(destination_airport__airport_country=destination)
        
        combined_data = zip(flight_info, schedule)
        
        context["combined_data"] = combined_data

        return context
    

class FlightRate(ListView):
    model = TicketPrice
    template_name = "flight_information/flight_rate.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        seats = TicketPrice.objects.all()

        seat_class = self.request.GET.get("seat_class")
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")

        if min_price:
            seats = seats.filter(price__gt =min_price ) # prices greater than 
        
        if max_price:
            seats = seats.filter(price__lt = max_price) # prices lesser than 

        if seat_class and seat_class != "Any":
            seats = seats.filter(seat_class = seat_class) # seat_class is the input name and the field in the table
        
        
        context["items"] = seats
        return context
    

class FlightInformation(ListView):
    model = flight_information
    template_name = "flight_information/flight_information.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flight_info = flight_information.objects.all()

        # get the fields from the departure and destination based on the names
        departure_country = self.request.GET.get("Departure", "")
        destination_country = self.request.GET.get("Destination", "")

        departure_date = self.request.GET.get("departure_date", "")
        arrival_date = self.request.GET.get("arrival_date", "")


        flight_number = self.request.GET.get("flight_number", "")
        seat_class = self.request.GET.get("classes", "")


        if seat_class and seat_class != "Any":
            flight_info = flight_info.filter(ticketprice__seat_class=seat_class)

        if departure_country and departure_country != "Any":
            flight_info = flight_info.filter(origin_airport__airport_country = departure_country)
        
        if destination_country and destination_country != "Any":
            flight_info = flight_info.filter(destination_airport__airport_country = destination_country)

        if departure_date and departure_date != "":
            flight_info = flight_info.filter(departure_date__date = departure_date)

        if arrival_date and arrival_date != "":
            flight_info = flight_info.filter(arrival_date__date = arrival_date)

        if flight_number and flight_number != "":
            flight_info = flight_info.filter(flight_number = flight_number)

        context["flights"] = flight_info
        return context
    