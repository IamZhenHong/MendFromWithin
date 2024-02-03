from django.db import models

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
class Order(models.Model):
    
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=100)
    session_key = models.CharField(max_length=100, blank=True)
    receipt = models.FileField(upload_to='receipts/', blank=True, null=True)
    order_summary = models.TextField(blank=True) 


    def __str__(self):
        return self.user
    