from django.shortcuts import render
from django.views.generic import CreateView
from buy_tickets.models import PaymentCard
from django.urls import reverse_lazy
from buy_tickets.forms import PaymentCardForm
from django.shortcuts import redirect


# Create your views here.
def CreatePaymentCard(request):
    if request.method == 'POST':
        payment_card_form = PaymentCardForm(request.POST)
        if payment_card_form.is_valid():
            payment_card_form = payment_card_form.save(commit=False)
            payment_card_form.Passenger = request.user
            payment_card_form.save()

    payment_card_form = PaymentCardForm()
    payment_card_object = PaymentCard.objects.filter(Passenger=request.user)

    return render(
        request,
        "buy_tickets/payment_card.html",{
        "payment_card_form": payment_card_form,
        "payment_card_object": payment_card_object
        }
    )

def DeletePaymentCard(request):
    if request.method == 'POST':
        payment_card_object = PaymentCard.objects.filter(Passenger=request.user).delete()
        return redirect('payment_card')

