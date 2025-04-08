from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# sync db time with the server time
from django.utils.timezone import now
# Create your models here.

#compare the dates
from datetime import timedelta


# plane info
class airplane_info(models.Model):
    airplane_id = models.BigIntegerField()
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=25)
    passenger_capacity = models.BigIntegerField()
    
    def __str__(self):
        return f"Airplane : {self.airplane_id}"
        
# flight schedule
class flight_schedule(models.Model):
    date = models.DateField()
    hour = models.DateTimeField()

    @property
    def status(self):
        #  Modifies the time part of self.hour (which is a DateTimeField) to be exactly midnight (00:00:00) while keeping the same date.
        # stores YYYY-MM-DD HH:MM:SS
        # scheduled_date_time = self.hour.replace(hour=0, minute=0, second=0)
        # now() gives a DateTime
        current_time = now()
        # check if a flight is in the past
        if self.date < current_time.date():
            return "Flight has already departed"
        elif self.date > current_time.date():
            return "Flight is in the future. Can be booked. "
        elif current_time.time() == self.hour:
            return "Flight is on time"
    
    def __str__(self):
        return f"Date: {self.date} - Hour: {self.hour} "

    
# airport
class airport(models.Model):
    airport_name = models.CharField(max_length=100)
    airport_country = models.CharField(max_length=100)
    airport_city = models.CharField(max_length=100)

    def __str__(self):
        return f"Airport : {self.airport_name} , Country : {self.airport_country}"
    
# flight information
class flight_information(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    origin_airport = models.OneToOneField(airport, on_delete=models.CASCADE, related_name="origin_airport")
    destination_airport = models.OneToOneField(airport, on_delete=models.CASCADE, related_name="destination_airport")
    arrival_date = models.OneToOneField(flight_schedule,  on_delete=models.CASCADE, related_name="arrival_date")
    departure_date = models.OneToOneField(flight_schedule, on_delete=models.CASCADE, related_name="departure_date")
    airplane_info = models.ManyToManyField(airplane_info)


    def __str__(self):
        return f"Flight number : {self.flight_number}"



# airline
class airline(models.Model):
    airline_name = models.CharField(max_length=100)
    flight = models.OneToOneField(flight_information, on_delete=models.CASCADE)