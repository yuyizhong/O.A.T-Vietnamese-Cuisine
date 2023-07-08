from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from math import floor


class Review(models.Model):
    RATING_CHOICES = (
        (0, '0 - Very Poor'),
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    )

    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = CloudinaryField('image', default=None, blank=True, null=True)
    visit_date = models.DateField()
   

    class Meta:
        """ Order by time of creation """
        ordering = ["-created_date"]

    def __str__(self):
        return f"Review for {self.menu_item.name} by {self.user.username}"

    @classmethod
    def average_rating(cls, menu_item):
        reviews = cls.objects.filter(menu_item=menu_item)
        if reviews.exists():
            total_rating = sum(review.rating for review in reviews)
            return total_rating / reviews.count()
        else:
            return 0
    @classmethod
    def full_stars(cls, menu_item):
        average_rating = cls.average_rating(menu_item)
        return floor(average_rating)