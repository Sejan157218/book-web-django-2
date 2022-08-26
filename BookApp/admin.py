from django.contrib import admin
from .models import *
# Register your models here.



admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(CartProduct)
admin.site.register(Order)

