from re import template
from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from accounts.views import LoginView,logout_view

app_name="accounts"
urlpatterns = [
    path('signup/', views.signupPage,name='signup'),
    # path('login/', views.loginPage,name='login'),
    path('logout/', logout_view,name='logout'),

   
    path('login/', LoginView.as_view(), name='login'),
    path('otp-phone-number/', views.OtpPhone, name='otp-phone-number'),
    path('confirmOtp/<str:pk>', views.confirmOtp, name='confirmOtp'),
    path('sentOtp/', views.sentOtp, name='sentOtp'),
    path('verifyOtp/', views.VerifyOtp, name='verifyOtp'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    # path('signup/', RegisterView.as_view(), name='signup')
]