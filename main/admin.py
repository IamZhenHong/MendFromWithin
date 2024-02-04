from django.contrib import admin
from .models import Item, CartItem, Order, ItemImage, User

# Register your models here.
class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1


admin.site.register(Item, ItemAdmin)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(ItemImage)
admin.site.register(User)
