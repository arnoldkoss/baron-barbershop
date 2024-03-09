from django.test import TestCase
from django.urls import reverse


class ReservationViewTest(TestCase):

    def test_reservation_view_get_request(self):
        """
        Test the reservation view with a GET request to ensure
        the form is rendered properly.
        """
        response = self.client.get(reverse('reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reservation/reservation.html')
        self.assertTrue('form' in response.context)
