from django.urls import path
from . import views

app_name='bookapp'

urlpatterns = [
    path('cartproducts', views.index, name='cartproducts'),
    path('', views.Home, name='home'),
    path('cart', views.Cart, name='cart'),
    path('search', views.Search, name='search'),
    path('category/<str:pk>', views.CategorySearch, name='category'),
    path('author/<str:pk>', views.AuthorSearch, name='author'),
    path('details/<str:pk>', views.BookDetails, name='details'),
    path('increase/<int:pk>', views.increaseItem, name='increase'),
    path('remove/<int:pk>', views.removeItem, name='remove'),
    path('delete/<int:pk>', views.deleteItem, name='delete'),
    path('myorder', views.myOrder, name='myorder'),
    path('order', views.OrderItem, name='order'),

]