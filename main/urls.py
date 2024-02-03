from django.contrib import admin
from django.urls import path
from main import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.landing, name="landing"),
    path("catalog/<str:category>/", views.product_catalog, name="product_catalog"),
    path("cart/", views.cart_view, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("product/<str:name>/", views.product_info, name="product_info"),
    path("add_to_cart/<str:name>/<int:quantity>/<str:size>/", views.add_to_cart, name="add_to_cart"), 
    path("order_success/", views.order_success, name="order_success"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
