from django import forms
from flight_reservation.models import book_flight, seat
from flight_information.models import flight_information
from django.forms import inlineformset_factory

# the user can only "book_flight"  to a "flight_information"
# manually associate that "book_flight" to the "flight_information" in the views
class BookFlightForm(forms.ModelForm):
    class Meta:
        model = book_flight
        fields = ["payment_card", "flight"] 


class SeatForm(forms.ModelForm):
    class Meta:
        model = seat
        fields = ['seat_class', 'row', 'letter']
        widgets = {
            'seat_class': forms.Select(attrs={'class': 'form-control'}),
            'row': forms.Select(attrs={'class': 'form-control'}),
            'letter': forms.Select(attrs={'class': 'form-control'}),
        }


# the user can book many "seats" to a "flight_information" table 
# the inline form automatically associates the many "seats" to the "flight_information"
SeatFormSet = inlineformset_factory(
    flight_information,
    seat,
    form=SeatForm,
    fields=('seat_class', 'row', 'letter'),
    extra=0,
    min_num=1,
    max_num=10,  # Maximum seats per booking
    can_delete=False,
)