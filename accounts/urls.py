from django.urls import path,include
from . import views
from accounts.views import LoginView,logout_view

app_name="accounts"
urlpatterns = [
    path('signup/', views.signupPage,name='signup'),
    # path('login/', views.loginPage,name='login'),
    path('logout/', logout_view,name='logout'),

   
    path('login/', LoginView.as_view(), name='login'),
    # path('signup/', RegisterView.as_view(), name='signup')
]