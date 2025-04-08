from django.db import models
from user_management.models import CustomUser
from flight_information.models import flight_information
# Create your models here.

# credit/debit card information
class PaymentCard(models.Model):
    number = models.CharField(max_length=16, unique=True)
    expiration_date = models.DateField()
    card_name = models.CharField(max_length=20)
    company_card = models.CharField(max_length=20)
    # Passenger can exist without a card, but a card must belong to a passenger.
    Passenger = models.OneToOneField(CustomUser, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Card name : {self.card_name}"

# flight rate (class?)
class TicketPrice(models.Model):
    seat_class = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    flight = models.ForeignKey(flight_information, on_delete=models.CASCADE)
