from django import forms
from .models import Reservation
from datetime import datetime, time, timedelta, date

def generate_time_choices():
    def time_range(start, end, delta):
        current = start
        while current <= end:
            yield current
            current = (datetime.combine(date.min, current) + delta).time()

    start = time(9, 0)  # Start time (9:00)
    end = time(17, 30)  # End time (17:30)
    delta = timedelta(minutes=30)  # Interval between times

    return [(t.strftime('%H:%M'), t.strftime('%H:%M')) for t in time_range(start, end, delta)]

class ReservationForm(forms.ModelForm):
    time = forms.ChoiceField(choices=generate_time_choices())

    class Meta:
        model = Reservation
        fields = ['name', 'date', 'time', 'gender']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }