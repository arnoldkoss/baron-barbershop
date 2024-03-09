from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):
    """
    Test to ensure the form is considered valid when the body has content.
    """
    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'This is a great post'})
        self.assertTrue(comment_form.is_valid())
    """
    Test to ensure the form is considered invalid when the body is empty.
    """
    def test_form_is_invalid(self):
        comment_form = CommentForm({'body': ''})
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
