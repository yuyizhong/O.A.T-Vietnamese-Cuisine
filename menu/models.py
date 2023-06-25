from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# from .models import Review


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    # Choice fields
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
        ('hidden', 'Hidden'),
    )

    name = models.CharField(max_length=60)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    menu_image = CloudinaryField('image', default='placeholder')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    class Meta:
        """ Order by type and name """
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    @property
    def formatted_price(self):
        return '£{:.2f}'.format(self.price)

    @property
    def average_rating(self):
        original_reviews = self.review_set.exclude(user__is_staff=True)
        if original_reviews.exists():
            total_rating = sum(review.rating for review in original_reviews)
            return total_rating / original_reviews.count()
        else:
            return 0
