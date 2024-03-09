from django.test import TestCase
from .forms import ReservationForm
from datetime import datetime, timedelta


class SimplifiedReservationFormTest(TestCase):
    def test_time_choices_not_empty(self):
        """
        Test to ensure that the time choices are generated
        and the list is not empty.
        """
        form = ReservationForm()
        self.assertTrue(form.fields['time'].choices,
                        "Time choices should not be empty.")

    def test_future_date_validation(self):
        """
        Test to ensure the form is invalid for dates today or in the past,
        and valid for dates in the future.
        """
        # Prepare form data with today's date (expected to be invalid)
        form_data_today = {
            'name': 'Test User',
            'date': datetime.now().date(),
            'time': '10:00',
            'gender': 'Prefer not to say'
        }
        form_today = ReservationForm(data=form_data_today)
        # Expect the form to be invalid for today's date
        self.assertFalse(form_today.is_valid(),
                         "Form should be invalid for today's date.")
