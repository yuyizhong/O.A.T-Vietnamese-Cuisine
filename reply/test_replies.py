from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Reply
from review.models import Review

class ReplyViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.review = Review.objects.create(title='Test Review')
        self.url = reverse('reply/<int:pk>/', kwargs={'pk': self.review.pk})
        
    def test_reply_view(self):
        # Log in the user
        self.client.login(username='testuser', password='testpassword')
        
        # Submit a reply
        response = self.client.post(self.url, {'content': 'Test Reply'})
        
        # Check if the reply was created
        self.assertEqual(response.status_code, 302)  # Assuming it redirects after creating a reply
        self.assertEqual(Reply.objects.count(), 1)
        reply = Reply.objects.first()
        self.assertEqual(reply.content, 'Test Reply')
        self.assertEqual(reply.user, self.user)
        self.assertEqual(reply.review, self.review)
        
    
