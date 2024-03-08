from django.core.exceptions import ValidationError
from django import forms
from datetime import datetime, time, timedelta, date
from .models import Reservation


def generate_time_choices():
    """
    Generates a list of time choices in 30-minute intervals
    between 9:00 and 17:30.

    This function creates a sequence of time
    slots starting from 9:00 AM to 5:30 PM
    with a 30-minute interval between each slot.
    The time slots are formatted as strings
    in the 'HH:MM' format.

    Returns:
        list of tuple: A list where each tuple contains
        the same time string twice,
        intended for use as choices in a Django form field.
    """
    def time_range(start, end, delta):
        """
        Generator function to create a range of times from
        start to end with a given interval.

        Args:
            start (datetime.time): The start time.
            end (datetime.time): The end time.
            delta (datetime.timedelta):
            The interval between each time in the range.

        Yields:
            datetime.time: The next time in the range.
        """
        current = start
        while current <= end:
            yield current
            current = (datetime.combine(date.min, current) + delta).time()

    start = time(9, 0)
    end = time(17, 30)
    delta = timedelta(minutes=30)

    return [(t.strftime('%H:%M'), t.strftime('%H:%M')) for t in time_range(start, end, delta)]


class ReservationForm(forms.ModelForm):
    """
    A form for creating and editing Reservation instances.

    This form uses the Reservation model and specifies
    fields for name, date, time,
    and gender. It also customizes the date input widget
    and validates the date to
    ensure it is at least one day in the future.
    """
    time = forms.ChoiceField(choices=generate_time_choices())

    class Meta:
        """
        Meta options for ReservationForm.

        Specifies the model to use for the form,
        the fields to include, and customizes
        the widget for the 'date' field.
        """
        model = Reservation
        fields = ['name', 'date', 'time', 'gender']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean_date(self):
        """
        Validates that the selected date is at least one day in the future.

        Raises:
            ValidationError: If the selected date is
            not at least one day in the future.

        Returns:
            datetime.date: The validated date.
        """
        input_date = self.cleaned_data.get('date')
        today = datetime.now().date()
        if input_date is not None and input_date <= today:
            raise ValidationError("Book at least 1 day ahead!")
        return input_date
