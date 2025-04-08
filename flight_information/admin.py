from django.contrib import admin
from .models import flight_information, airport, flight_schedule, airplane_info, airline

# Customize Flight Admin
class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_number', 'origin_airport', 'destination_airport')  # Columns in admin list
    search_fields = ('flight_number',)  # Search by flight number
    list_filter = ('origin_airport', 'destination_airport')  # Filter flights by airports

# Registering the models
admin.site.register(flight_information, FlightAdmin)
admin.site.register(airport)
admin.site.register(flight_schedule)
admin.site.register(airplane_info)
admin.site.register(airline)
