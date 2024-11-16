from django.urls import path
from. import views
from django.contrib.auth import views as auth_views
from django.urls import reverse


urlpatterns = [
    path('', views.base, name='base'),
    path('registration.html/',views.register_page,name='registration'),
    path('login/', views.login_page, name='login_page'),

    path('dashboard/',views.dashboard_page,name='dashboard'),
    # path('', views.base_page, name='base'),  # Your base page
    # path('logout/', views.LogoutView, name='logout'),
    path('about us/',views.About_us,name='about'),
    path('', views.home, name='home'),
    path('logout',views.lg,name='logout'),
    path('forgot',views.fg,name='forgot'),
    path('CLogin.html/',views.CLogin,name='CLogin'),

    path('managerLogin.html/', views.vijay_view, name='vijay'),
    path('Cdashboard.html/', views.Cdashboard, name='Cdashboard'),
    path('overview.html/',views.overview,name='overview'),
    path('/', views.contact, name='contact'),
    path('terms.html/', views.terms, name='terms'),
    path('certificate.html/', views.Certificate, name='certificate'),
    path('DeveloperGuide/',views.Guide,name='DeeveloperGuide'),
    path('details.html/', views.details, name='details'),
    path('report.html/', views.report, name='report'),
    path('cfeedback.html/', views.cfeedback, name='feedback'),


    path('manager-login/', views.manager_login, name='manager_login'),
    path('my_customers/', views.my_customers, name='my_customers'),
    path('customer/<int:customer_id>/', views.customer_detail, name='customer_detail'),


    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard URL# Dashboard URL
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),

    path('my_customers/', views.my_customers, name='my_customers'),
    path('login/', views.login_view, name='login'),
    path('profile/', views.profile_view, name='profile'),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('order-details/<str:status>/', views.order_details, name='order_details'),
    path('add-order/', views.add_order, name='add_order'),

    path('view_pending_orders/', views.view_pending_orders, name='view_pending_orders'),
    path('view_delivered_orders/', views.view_delivered_orders, name='view_delivered_orders'),
    path('my_orders/', views.user_orders, name='user_orders'),

    path('customer-orders/', views.customer_orders, name='customer_orders'),

    # URL for editing a specific order
    path('edit-order/<int:order_id>/', views.edit_order, name='edit_order'),
    path('customer/<int:id>/', views.view_customer_profile, name='view_customer_profile'),
    path('my-customers/', views.my_customers, name='my_customers'),
path('submit-feedback/', views.submit_feedback, name='submit_feedback'),
]