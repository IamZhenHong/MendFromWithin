from django.shortcuts import render
from .models import Item, CartItem, Order
from .forms import CheckoutForm, PaymentForm
from django.shortcuts import redirect
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from django.http import JsonResponse
from django.shortcuts import get_object_or_404 
# Create your views here.


def landing(request):
    return render(request, "main/landing.html")



def product_catalog(request, category):
    items = Item.objects.filter(category=category)
    context = {
        "items": items,
    }
    return render(request, "main/product_catalog.html", context)

def product_info(request, name):
    item = Item.objects.get(name=name)
    context = {
        "item": item,
    }
    return render(request, "main/product_info.html", context)

def cart_view(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(Q(user=request.user) )
    total_price = sum(item.item.price * item.quantity for item in cart_items)
    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }
    return render(request, "main/cart.html", context)

def add_to_cart(request, name, quantity=1,size=None):
    item = get_object_or_404(Item, name=name)

    cart_item, created = CartItem.objects.get_or_create(user=request.user, item=item,size = size,defaults={'quantity': quantity})

    if not created:
        cart_item.quantity += quantity
        cart_item.save()

    print(f"Added {quantity} {item.name}(s) to the cart. New quantity: {cart_item.quantity}")

    response_data = {
        'message': f"Added {quantity} {item.name}(s) of size {size} to the cart. New quantity: {cart_item.quantity}",
        'item_name': item.name,
        'quantity': cart_item.quantity,
        'size': cart_item.size
    }

    return JsonResponse(response_data)

def remove_from_cart(request, name, size=None):
    item = get_object_or_404(Item, name=name)

    # Get the cart item based on the user, item, and optional size
    cart_item = get_object_or_404(CartItem, user=request.user, item=item, size=size)

    # Delete the cart item
    cart_item.delete()

    response_data = {
        'message': f"Removed {item.name} from the cart.",
        'item_name': item.name,
        'size': size
    }

    return JsonResponse(response_data)


def checkout(request):
    session_key = request.session.session_key
    cart_items = CartItem.objects.filter(user=request.user)
    print(cart_items)
    order_summary = ', '.join([f"{item.quantity} {item.size} {item.item.name}" for item in cart_items])
    print(order_summary)
    total_amount = sum(item.item.price * item.quantity for item in cart_items)

    if request.method == 'POST':
        checkout_form = CheckoutForm(request.POST)
        payment_form = PaymentForm(request.POST, request.FILES)

        if checkout_form.is_valid() and payment_form.is_valid():
            # Check the selected delivery option and adjust the total amount
            delivery_option = checkout_form.cleaned_data.get('delivery_option')
            if delivery_option == 'delivery':
                total_amount += 10
            name = checkout_form.cleaned_data['name']

            order = Order.objects.create(user=name, session_key=session_key, total=total_amount)

            # Add CartItem instances to the order
            for cart_item in cart_items:
                cart_item.order = order
                cart_item.save()
            
            order.order_summary = order_summary
            order.receipt = payment_form.cleaned_data['receipt']
            order.save()
            print(cart_items)

            # Process the payment, generate QR code, etc.

            cart_items.delete()
            return redirect('order_success')
    else:
        checkout_form = CheckoutForm()
        payment_form = PaymentForm()

    return render(request, 'main/checkout.html', {'checkout_form': checkout_form, 'payment_form': payment_form, 'total_amount': total_amount, 'cart_items': cart_items})
def order_success(request):
    return render(request, 'main/order_success.html')