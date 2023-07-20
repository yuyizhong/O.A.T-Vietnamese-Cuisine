from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    """ Model to create Categories """
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    """ Model to create Menu """    

    """ Choice fields """
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
        """ Order by menu category and name """
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

    # price decoration
    @property        
    def formatted_price(self):
        return '£{:.2f}'.format(self.price)
