from .models import Remote_bookings
from django.forms import ModelForm


class RemoteBookingForm(ModelForm):
    class Meta:
        model=Remote_bookings
        fields='__all__'