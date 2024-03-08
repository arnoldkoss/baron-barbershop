from django.core.exceptions import ValidationError
from django import forms
from datetime import datetime, time, timedelta, date
from .models import Reservation


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
    
    def clean_date(self):
        input_date = self.cleaned_data.get('date')
        today = datetime.now().date()
        if input_date is not None and input_date <= today:
            raise ValidationError("The date must be at least one day in the future.")
        return input_date