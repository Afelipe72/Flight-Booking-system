from django.db import models
from buy_tickets.models import PaymentCard
from flight_information.models import flight_information
# Create your models here.

class book_flight(models.Model):
    booking_code = models.CharField(max_length=20, unique=True)
    payment_card = models.ForeignKey(PaymentCard, on_delete=models.CASCADE)
    flight = models.ForeignKey(flight_information, on_delete=models.CASCADE)

# seat
class seat(models.Model):
    
    ROW_CHOICES = [(str(i), str(i)) for i in range(1, 31)]
    
    LETTER_CHOICES = [(chr(i), chr(i)) for i in range(65, 71)]  # A-F


    SEAT_CLASS_CHOICES = [
        ('Business Class', 'Business Class'),
        ('Economy Class', 'Economy Class'),
        ('First Class', 'First Class'),
    ]


    seat_class = models.CharField(max_length=20, choices=SEAT_CLASS_CHOICES)
    row = models.CharField(max_length=3, choices=ROW_CHOICES)
    letter = models.CharField(max_length=1, choices=LETTER_CHOICES)
    flight = models.ForeignKey(flight_information, on_delete=models.CASCADE)