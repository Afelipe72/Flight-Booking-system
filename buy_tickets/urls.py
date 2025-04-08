from django.urls import path
from buy_tickets.views import CreatePaymentCard, DeletePaymentCard
urlpatterns = [
    path('', CreatePaymentCard, name='payment_card'),
    path('Delete-payment-card/', DeletePaymentCard, name='delete_payment_card'),
]
