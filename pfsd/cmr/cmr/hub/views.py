from urllib import request

from django.core.checks import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from psycopg2 import IntegrityError

from .models import Customer  # Import your Customer model


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Customer  # Import your Customer model
from django.contrib.auth.models import User
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User
from .models import Customer
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import IntegrityError

def register_page(request):
    if request.method == 'POST':
        # Get data from the form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate that passwords match
        if password != confirm_password:
            error_message = "Your password and confirm password are not the same!"
            return render(request, 'hub/registration.html', {'error_message': error_message})

        try:
            # Create user if passwords match
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )

            # Automatically log the user in
            login(request, user)

            # Redirect to a successful login or dashboard page
            return redirect('CLogin')  # Change 'CLogin' to the appropriate URL name for your site

        except IntegrityError as e:
            # Handle cases where user already exists or other integrity errors
            error_message = "An error occurred during registration: " + str(e)
            return render(request, 'hub/registration.html', {'error_message': error_message})

    return render(request, 'hub/registration.html')


def login_page(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate user credentials
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            # Return success response for AJAX
            return JsonResponse({'status': 'success'})
        else:
            # Return error response for AJAX
            return JsonResponse({'status': 'error', 'message': 'Username or password is incorrect!'})

    # If it's a GET request, render the login page
    return render(request, 'hub/manager.html')



from django.shortcuts import render, redirect

# views.py
from django.contrib.auth.decorators import login_required
def profile(request):
    if request.method == 'POST':
        # Update the profile details
        user = request.user

        user.save()
        messages.success(request, "Profile updated successfully!")
        return redirect('profile')  # Redirect to the profile page after saving changes

    # For GET request, display the profile details
    return render(request, 'hub/cdashboard.html')


from django.shortcuts import render
from .models import Customer, Order

from django.shortcuts import render, redirect
from .models import Customer


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']

        email = request.POST['email']


        # Create a new customer and save it
        customer = Customer.objects.create(
            first_name=first_name,

            email=email,

        )
        return redirect('my_customers')  # Redirect to the customers list

    return render(request, 'hub/register.html')


from django.shortcuts import render
from django.contrib.auth.models import User


def my_customers(request):
    # Fetch all registered users
    users = User.objects.all()

    # Pass the users to the template
    return render(request, 'my_customers.html', {'users': users})


from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

def manager_login(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user with the provided credentials
        user = authenticate(request, username=uname, password=password)

        if user is not None:
            # Check if the user is a superuser (admin)
            if user.is_superuser:
                # Log the user in
                login(request, user)
                # Redirect to manager dashboard or wherever the superuser should go
                return redirect('dashboard')  # Redirect to the desired view
            else:
                # If the user is not a superuser, show an error message
                messages.error(request, 'You do not have admin privileges!')
        else:
            # If authentication fails, show an incorrect credentials error message
            messages.error(request, 'Incorrect username or password!')

    # Render the manager login page if it's a GET request
    return render(request, 'hub/managerLogin.html')

from django.shortcuts import render
from .models import Customer  # Assuming you have a Customer model

def my_customers(request):
    # Fetch all customers from the database
    customers = Customer.objects.all()

    # Render the template and pass the customer data
    return render(request, 'hub/my_customers.html', {'customers': customers})


def customer_detail(request, customer_id):
    # Fetch customer by ID
    customer = get_object_or_404(Customer, id=customer_id)
    return render(request, 'hub/customer_detail.html', {'customer': customer})
@login_required
def dashboard_page(request):
    return render(request, 'hub/dashboard.html')


# Other views (unchanged)
def base(request):
    return render(request, 'hub/base.html')

def CLogin(request):
    return render(request, 'hub/CLogin.html')

def Cdashboard(request):
    return render(request, 'hub/Cdashboard.html')

# You can add more views as needed...
# Dashboard pa
# ge - Only accessible to logged-in users






def lg(request):
    return render(request, 'hub/manager.html')


def About_us(request):
    return render(request, 'hub/about.html')


def overview(request):
    return render(request, 'hub/overview.html')


def contact(request):
    return render(request, 'hub/contact.html')


def home(request):
    return render(request, 'hub/base.html')


def terms(request):
    return render(request, 'hub/terms.html')




def fg(request):
    return render(request, 'hub/forgot.html')


def CLogin(request):
    return render(request, 'hub/CLogin.html')

# def login_page(request):
#     return render(request, 'manager.html')


def Certificate(request):
    return render(request, 'hub/certificate.html')


def Cdashboard(request):
    return render(request, 'hub/Cdashboard.html')


def cfeedback(request):
    return render(request, 'hub/cfeedback.html')


def cprofile(request):
    return render(request, 'hub/cprofile.html')


def Guide(request):
    return render(request, 'hub/DeveloperGuide.html')


def details(request):
    return render(request, 'hub/details.html')


def report(request):
    return render(request, 'hub/report.html')

def dashboard(request):
    return render(request, 'dashboard.html')


from django.shortcuts import render

def vijay_view(request):
    return render(request, 'hub/managerLogin.html')

def manager_dashboard(request):
    # Logic for manager dashboard
    return render(request, 'hub/dashboard.html')


def my_customers_view(request):
    # Fetch all customers
    customers = Customer.objects.all()
    return render(request, 'hub/my_customers.html', {'customers': customers})

# views.py
from django.shortcuts import render
from .models import Customer

def my_customers(request):
    customers = Customer.objects.all()  # Fetch all customers from the database
    return render(request, 'hub/my_customers.html', {'customers': customers})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# If you have a custom view for login, you can use:
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')  # Redirect to profile after login
    return render(request, 'login.html')
@login_required
def profile_view(request):
    user_profile = request.user.profile  # Access the UserProfile model
    return render(request, 'profile.html', {'profile': user_profile})
# views.py
from django.contrib.auth import logout
from django.shortcuts import redirect


# hub/views.py

from django.shortcuts import render, redirect
from .models import Customer, Order
from .forms import CustomerForm, OrderForm

def register_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer = customer_form.save()  # Save the customer object
            return redirect('add_order', customer_id=customer.id)  # Redirect to the order creation page
    else:
        customer_form = CustomerForm()

    return render(request, 'register_customer.html', {'form': customer_form})


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Order, Customer
from .forms import OrderForm
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from .models import Order
# views.py
from django.shortcuts import render, redirect
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product  # Assuming your model is named 'Product'
from django.http import JsonResponse
from .models import Product
from django.contrib.auth.decorators import login_required

@login_required
def add_order(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # Check for AJAX request
        try:
            # Extract form data
            order_name = request.POST.get('order_name')
            status = request.POST.get('status')
            description = request.POST.get('description')

            # Create the order object (assuming your model is named Product)
            product = Product.objects.create(
                order_name=order_name,
                status=status,
                description=description,
                user=request.user  # Automatically set the logged-in user
            )

            # Get the updated order counts for the logged-in user
            total_orders = Product.objects.filter(user=request.user).count()
            pending_orders = Product.objects.filter(user=request.user, status='Pending').count()
            delivered_orders = Product.objects.filter(user=request.user, status='Delivered').count()

            # Return the data in JSON format
            return JsonResponse({
                'total_orders': total_orders,
                'pending_orders': pending_orders,
                'delivered_orders': delivered_orders,
            })

        except Exception as e:
            # Return an error response if something goes wrong
            return JsonResponse({'error': str(e)}, status=500)

    else:
        # If not a valid AJAX request, return an error
        return JsonResponse({'error': 'Invalid request or not an AJAX request'}, status=400)


from django.http import JsonResponse
from .models import Product

def order_details(request, status):
    # Get the orders by status for the logged-in user
    orders = Product.objects.filter(user=request.user, status=status)
    order_data = [{
        'name': order.name,
        'description': order.description
    } for order in orders]

    return JsonResponse({'orders': order_data})

@login_required
def dashboard(request):
    # Get all orders for the current logged-in user
    total_orders = Product.objects.filter(user=request.user).count()
    pending_orders = Product.objects.filter(user=request.user, status='Pending').count()
    delivered_orders = Product.objects.filter(user=request.user, status='Delivered').count()

    return render(request, 'Cdashboard.html', {
        'total_orders': total_orders,
        'pending_orders': pending_orders,
        'delivered_orders': delivered_orders,
    })
def dashboard(request):
    order_status = "Pending"  # Get this dynamically based on user's orders
    return render(request, 'dashboard.html', {'order_status': order_status})

# views.py

from django.shortcuts import render
from django.http import JsonResponse
from .models import Order  # Assuming you have an Order model

def order_details(request):
    user_id = request.GET.get('user_id')
    status = request.GET.get('status')

    # Get the user's orders based on the status (Pending or Delivered)
    orders = Order.objects.filter(user_id=user_id, status=status)

    order_list = []
    for order in orders:
        order_list.append({
            'name': order.name,
            'status': order.status,
            'description': order.description,
            'created_at': order.created_at.strftime('%b %d, %Y'),
        })

    return JsonResponse({'orders': order_list})
# views.py
from django.shortcuts import render
from .models import Order  # Assuming you have an Order model

# views.py
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Order  # Assuming you have an Order model with a 'status' field

# View for fetching pending orders
def view_pending_orders(request):
    user_id = request.GET.get('user_id')  # Get user ID from the query params
    if user_id:
        orders = Order.objects.filter(status='Pending', user_id=user_id)  # Adjust for your model
    else:
        orders = Order.objects.filter(status='Pending')  # Fallback, if no user_id is passed

    order_list = list(orders.values('id', 'name', 'status', 'description', 'created_at'))  # Adjust based on your model fields
    return JsonResponse({'orders': order_list})

# View for fetching delivered orders
def view_delivered_orders(request):
    user_id = request.GET.get('user_id')
    if user_id:
        orders = Order.objects.filter(status='Delivered', user_id=user_id)
    else:
        orders = Order.objects.filter(status='Delivered')

    order_list = list(orders.values('id', 'name', 'status', 'description', 'created_at'))
    return JsonResponse({'orders': order_list})

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Order

@login_required
def user_orders(request):
    # Fetch the orders for the logged-in user
    orders = Order.objects.filter(user=request.user)

    # Pass the orders to the template
    return render(request, 'orders/user_orders.html', {'orders': orders})


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm  # Assuming you have a form for editing Product model

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product  # Assuming you want to retrieve all products

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product  # Assuming Product is your order model



from django.shortcuts import render
from django.http import JsonResponse
from .models import Order  # Adjust to your actual model

def view_my_orders(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user)  # Replace with actual filtering logic
        order_list = [
            {
                'name': order.name,
                'status': order.status,
                'description': order.description,
                'created_at': order.created_at.strftime('%b %d, %Y')
            }
            for order in orders
        ]
        return JsonResponse({'orders': order_list})

    return JsonResponse({'error': 'User not authenticated'}, status=401)

#from django.shortcuts import render
from .models import Order  # Assuming Order is your model for orders
from django.shortcuts import render
from .models import Order
# views.py
from django.shortcuts import render
from .models import Order  # Assuming your order model is in the same app
from django.db.models import Q  # For advanced queries like search
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product  # Assuming you want to retrieve all products

@login_required
def customer_orders(request):
    # Get all products (no filtering by user)
    orders = Product.objects.all()  # Fetch all products, not just the ones belonging to the logged-in user

    return render(request, 'hub/customer_orders.html', {'orders': orders})





@login_required
def edit_order(request, order_id):
    # Fetch the specific order by ID
    order = get_object_or_404(Product, id=order_id)

    # Handle the POST request for editing the order
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=order)
        if form.is_valid():
            form.save()  # Save the updated order
            return redirect('customer_orders')  # Redirect to the order list

    # If it's a GET request, render the edit form
    else:
        form = ProductForm(instance=order)

    return render(request, 'hub/edit_order.html', {'form': form, 'order': order})
@login_required
def dashboard(request):
    total_orders_count = Product.objects.filter(user=request.user).count()

    return render(request, 'dashboard.html', {
        'total_orders_count': total_orders_count,
    })
from django.shortcuts import render
from django.contrib.auth.models import User

# View to display all users
# views.py
from django.shortcuts import render
from django.contrib.auth.models import User

def my_customers(request):
    customers = User.objects.exclude(is_superuser=True)  # exclude admin users
    context = {
        'customers': customers
    }
    return render(request, 'hub/my_customers.html', context)  # Ensure the correct path here

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
import json

# views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Feedback
import json

@csrf_exempt  # Allow POST requests from the frontend
def submit_feedback(request):
    if request.method == 'POST':
        # Get data from the request body (JSON)
        data = json.loads(request.body)
        rating = data.get('rating')
        comments = data.get('comments')

        # Save feedback to the database
        if rating and comments:
            feedback = Feedback.objects.create(rating=rating, comments=comments)
            return JsonResponse({'message': 'Feedback submitted successfully!'}, status=200)
        else:
            return JsonResponse({'error': 'Missing rating or comments'}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)

from django.shortcuts import render

def view_customer_profile(request, id):
    # Logic to view a customer's profile
    return render(request, 'customer_profile.html', {'customer': customer})
