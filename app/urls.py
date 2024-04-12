from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('general-dashboard/', views.general_dashboard_view, name='general_dashboard_url_name'),
    path('ecommerce-dashboard/', views.ecommerce_dashboard_view, name='ecommerce_dashboard_url_name'),
    path('layout-default/', views.layout_default_view, name='layout_default_url_name'),
    path('blank/', views.blank_view, name='blank_url_name'),
    path('auth-forgot-password/', views.auth_forgot_password_view, name='auth_forgot_password_url_name'),
    path('auth-login/', views.auth_login_view, name='auth_login_url_name'),
    path('auth-login-2/', views.auth_login_2_view, name='auth_login_2_url_name'),
    path('auth-register/', views.auth_register_view, name='auth_register_url_name'),
    path('auth-reset-password/', views.auth_reset_password_view, name='auth_reset_password_url_name'),
    path('errors-503/', views.errors_503_view, name='errors_503_url_name'),
    path('errors-403/', views.errors_403_view, name='errors_403_url_name'),
    path('errors-404/', views.errors_404_view, name='errors_404_url_name'),
    path('errors-500/', views.errors_500_view, name='errors_500_url_name'),
    path('features-activities/', views.features_activities_view, name='features_activities_url_name'),
    path('utilities-contact/', views.utilities_contact_view, name='utilities_contact_url_name'),
    path('utilities-invoice/', views.utilities_invoice_view, name='utilities_invoice_url_name'),
    path('utilities-subscribe/', views.utilities_subscribe_view, name='utilities_subscribe_url_name'),
    path('credits/', views.credits_view, name='credits_url_name'),
]