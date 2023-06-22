from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Choice fields
class Menu(models.Model):
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
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)

    class Meta:
        """ Order by type and name """
        ordering = ['type', 'name']

    def __str__(self):
        return self.name

 