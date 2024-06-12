from django.db import models
from users.models import User
from django.contrib.auth.models import AbstractUser,UserManager


class furniture_item(models.Model):
    ITEM_TYPES = [
        ('sofa', 'Sofa'),
        ('table', 'Table'),
        ('footstool', 'Footstool'),
    ]

    item_name = models.CharField(max_length=200)
    item_description = models.TextField()
    item_type = models.CharField(max_length=50, choices=ITEM_TYPES)
    item_price = models.IntegerField()
    item_picture = models.ImageField(upload_to="item_picturs", height_field=None, width_field=None, max_length=None, default="item_picturs/product.png")
    item_rating = models.FloatField(default=0.0)
    num_reviews = models.IntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    rated_by = models.ManyToManyField(User)

    def __str__(self):
        return self.item_name

    def update_rating(self, new_rating, user):
        self.rated_by.add(user)
        self.item_rating = (self.item_rating * self.num_reviews + new_rating) / (self.num_reviews + 1)
        self.num_reviews += 1
        self.save()

    def get_rating(self):
        """
        Returns the item's current rating.
        """
        return self.item_rating
class cart(models.Model):
    items = models.ManyToManyField(furniture_item)
    cart_owner = models.OneToOneField(User, on_delete=models.CASCADE, null=True)

