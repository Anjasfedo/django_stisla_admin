from django.shortcuts import render

# Create your views here.

def dashboard(request):
    context = {}
    return render(request, 'dashboard.html', context)

def general_dashboard_view(request):
    return render(request, 'index-0.html')

def ecommerce_dashboard_view(request):
    return render(request, 'index.html')

def layout_default_view(request):
    return render(request, 'layout-default.html')

def blank_view(request):
    return render(request, 'blank.html')

def blank_page_view(request):
    return render(request, 'blank.html')

def bootstrap_alert_view(request):
    return render(request, 'bootstrap-alert.html')

def auth_forgot_password_view(request):
    return render(request, 'auth-forgot-password.html')

def auth_login_view(request):
    return render(request, 'auth-login.html')

def auth_login_2_view(request):
    return render(request, 'auth-login-2.html')

def auth_register_view(request):
    return render(request, 'auth-register.html')

def auth_reset_password_view(request):
    return render(request, 'auth-reset-password.html')

def errors_503_view(request):
    return render(request, 'errors-503.html')

def errors_403_view(request):
    return render(request, 'errors-403.html')

def errors_404_view(request):
    return render(request, 'errors-404.html')

def errors_500_view(request):
    return render(request, 'errors-500.html')

def features_activities_view(request):
    return render(request, 'features-activities.html')

def utilities_contact_view(request):
    return render(request, 'utilities-contact.html')

def utilities_invoice_view(request):
    return render(request, 'utilities-invoice.html')

def utilities_subscribe_view(request):
    return render(request, 'utilities-subscribe.html')

def credits_view(request):
    return render(request, 'credits.html')