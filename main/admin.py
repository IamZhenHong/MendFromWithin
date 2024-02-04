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
    list_display = ['id', 'user_info', 'get_phone_number', 'total', 'date']
    list_display_links = ['id', 'user_info']

    def user_info(self, obj):
        return f"{obj.user.username} "

    user_info.short_description = 'User Information'

    def get_phone_number(self, obj):
        return obj.user.phone_number

    get_phone_number.short_description = 'Phone Number'

admin.site.register(Item, ItemAdmin)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(ItemImage)
admin.site.register(User)
