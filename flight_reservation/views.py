from django.shortcuts import render, redirect
from django.views.generic import View
from flight_reservation.forms import BookFlightForm, SeatFormSet

def ticket_reservation(request):
    if request.method == 'POST':
        book_flight_form = BookFlightForm(request.POST)
        book_seat_form = SeatFormSet(request.POST)
        if book_flight_form.is_valid() and book_seat_form.is_valid(): 
            booking_save = book_flight_form.save(commit=False)
            booking_save.user = request.user  # Attach the logged-in user
            booking_save.save()

            seat_save = book_seat_form.save(commit=False)
            for seat in seat_save:
                # booking_save.flight retrieves the flight_information object linked to that booking
                seat.flight = booking_save.flight

            return redirect('flight_reservation')

    
    book_flight_form = BookFlightForm()
    book_seat_form = SeatFormSet()
    
    return render( request,
        "flight_reservation/flight_reservation.html", {
        "book_flight_form": book_flight_form,
        "book_seat_form": book_seat_form
    })