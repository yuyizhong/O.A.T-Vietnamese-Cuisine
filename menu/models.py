from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Choice fields


class MenuItem(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    )

    TYPE_CHOICES = (
        ('appetizer', 'Appetizer'),
        ('main_course', 'Main Course'),
        ('dessert', 'Dessert'),
        ('beverage', 'Beverage'),
    )

    name = models.CharField(max_length=60)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=4, decimal_places=2)
    menu_image = CloudinaryField('image', default='placeholder')
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='draft')
    category = models.CharField(max_length=20, choices=TYPE_CHOICES)
    average_rating = models.FloatField(default=0)

    class Meta:
        """ Order by type and name """
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    @property
    def formatted_price(self):
        return '£{:.2f}'.format(self.price)

    def update_average_rating(self):
        total_reviews = self.reviews.count()
        if total_reviews > 0:
            total_ratings = sum(
                [review.rating for review in self.reviews.all()])
            self.average_rating = total_ratings / total_reviews
        else:
            self.average_rating = 0
        self.save()
