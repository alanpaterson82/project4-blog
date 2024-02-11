from django.test import TestCase
from django.urls import reverse
from .models import Background
from .forms import CollaborateForm


class TestBackgroundView(TestCase):

    def setUp(self):
        """Creates background content"""
        self.background_content = Background(
            title="Background", content="Background.")
        self.background_content.save()


    def test_render_background_page_with_collaborate_form(self):
        """Verifies get request for background containing a collaboration form"""
        response = self.client.get(reverse('background'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Background', response.content)
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)


    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
    post_data = {
        'name': 'test name',
        'email': 'test@email.com',
        'message': 'test message'
    }
    response = self.client.post(reverse('about'), post_data)
    self.assertEqual(response.status_code, 200)
    self.assertIn(
        b'Collaboration request received! I endeavour to respond within 2 working days.', response.content)