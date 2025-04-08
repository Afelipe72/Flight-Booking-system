from django.contrib import admin

# Register your models here.
from .models import PaymentCard, TicketPrice

admin.site.register(PaymentCard)
admin.site.register(TicketPrice)


