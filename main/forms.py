from django import forms

class CheckoutForm(forms.Form):
    name = forms.CharField(label='Name', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    shipping_address = forms.CharField(label='Shipping Address', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    delivery_option = forms.ChoiceField(
        label='Delivery Option',
        choices=[('delivery', 'Delivery +$10'), ('pickup', 'Pickup')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
   
    phone_number = forms.CharField(label='Phone Number', required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    # Add other fields as needed for the checkout process


class PaymentForm(forms.Form):
  
    receipt = forms.ImageField(label='Transaction Receipt', required=True)
    # Add other payment fields as needed