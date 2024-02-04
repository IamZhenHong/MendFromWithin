from django.db import models
from django.contrib.auth.models import AbstractUser 
from django.contrib.auth import get_user_model 
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
# Create your models here.

class Item(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    stock = models.IntegerField(blank=True, null=True)  # Using null=True for integer fields with blank option
    price = models.IntegerField()

    def __str__(self):
        return self.name
    
class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images")

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    user = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, blank=True, null=True)
    session_key = models.CharField(max_length=100, blank=True)




    def __str__(self):
        return f"{self.quantity} of {self.size} {self.item.name}"
    
class User(models.Model):
 
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255, blank=True)
    shipping_address = models.CharField(max_length=255, blank=True)
    delivery_option = models.CharField(max_length=10, blank=True, choices=[('delivery', 'Delivery +$10'), ('pickup', 'Pickup')])
    phone_number = models.CharField(max_length=20, blank=True)
    receipt = models.ImageField(upload_to='receipts/', blank=True, null=True)


    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return f" {self.name}  "

    
class Order(models.Model):
    items = models.ManyToManyField(Item, through='CartItem')
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session_key = models.CharField(max_length=100, blank=True)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)
    order_summary = models.TextField(blank=True) 


    def __str__(self):
        return f"Order for {self.user.username}"
    