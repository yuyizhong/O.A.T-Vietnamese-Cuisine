from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from review.models import Review

class Reply(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reply to {self.review} by {self.user.username}"
