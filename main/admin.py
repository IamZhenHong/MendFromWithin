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

class OrderAdmin(admin.ModelAdmin):
    inlines = [CartItemInline]
    list_display = [ 'get_phone_number']
    list_display_links = ['user']

    def get_phone_number(self, obj):
        return obj.user.phone_number

    get_phone_number.short_description = 'Phone Number'

admin.site.register(Item, ItemAdmin)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(ItemImage)
admin.site.register(User)
