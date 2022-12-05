from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register_customer_account, name='SignUp'),
    path('register/specialrole', views.register_non_customer_account, name='Register'),
    path('login/', views.login_account, name='SignIn'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('account/profile/', views.customer_profile , name='customer-profile'),
    path('vendor/profile/', views.vendor_profile , name='vendor-profile'),
    path('merchant/profile/', views.merchant_profile , name='merchant-profile'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer/dashboard/', views.customer_dashboard, name='customer-dashboard'),
]