from django.contrib import admin
from .models import Item, CartItem, Order, ItemImage

# Register your models here.
class ItemImageInline(admin.TabularInline):  # or admin.StackedInline for a different layout
    model = ItemImage
    extra = 1  # Number of empty forms to display for adding new images

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

admin.site.register(Item, ItemAdmin)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(ItemImage)