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
        
    