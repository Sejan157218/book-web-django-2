from django.urls import path
from . import views

app_name='bookapp'

urlpatterns = [
    path('', views.Home, name='home'),
    path('cart', views.Cart, name='cart'),
    path('search', views.Search, name='search'),
     path('category/<str:pk>', views.CategorySearch, name='category'),
     path('author/<str:pk>', views.AuthorSearch, name='author'),
    path('all-book', views.AllBook, name='all-book'),

]