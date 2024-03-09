from django.test import TestCase
from django.urls import reverse

class SimpleAboutMeViewTest(TestCase):

    def test_about_me_view_status_and_template(self):
        """
        Test to ensure the about_me view responds with a 200 status code
        and renders the expected about/about.html template.
        """
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')