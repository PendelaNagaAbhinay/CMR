from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from .models import Customer, Order



# Registration Form
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Login Form
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']


# hub/forms.py

from django import forms
from .models import Customer, Order

# hub/forms.py

from django import forms
from .models import Customer, Order

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']  # Include the fields you want for registration

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['order_date']  # Exclude 'order_date' since it is auto-generated

from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone']

# forms.py
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['order_name', 'status', 'description']  # Include the fields you want to display in the form
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['order_name', 'status', 'description']  # Add any other fields as necessary
