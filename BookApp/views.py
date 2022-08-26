from email import message
from unicodedata import category
from django.http import HttpResponse,JsonResponse
import json
from django.shortcuts import redirect,render
from .models import *
from django.contrib.postgres.search import SearchVector,SearchQuery
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages



def baseData(request):
    category =Category.objects.all();
    author =Author.objects.all();
    return {
        'category':category,
        'authors':author,
    }

def cartData(request):
     quantity=''
     if request.user.id !=None:
          cartProduct=CartProduct.objects.filter(user=request.user.email)
          quantity=sum(item.quantity for item in cartProduct)
     else:
          quantity=''
     return {
        'quantity':quantity,
    }



def Home(request):
     data =Book.objects.all()
     dramaCategory=Book.objects.filter(category__title="Drama").order_by('date')
     thrillerCategory=Book.objects.filter(category__title="Thriller").order_by('date')
     historyCategory=Book.objects.filter(category__title="History").order_by('date')
     return render(request, 'home.html',{'data':data,'dramaCategory':dramaCategory,'thrillerCategory':thrillerCategory,'historyCategory':historyCategory})



def Search(request):
     if 'search-text' in request.GET:
        book_name =  request.GET['search-text']
     #    data=Book.objects.filter(author__name=book_name) or Book.objects.filter(category__title=book_name) or Book.objects.filter(title=book_name)
        data=Book.objects.annotate(search=SearchVector('category__title', 'author__name','title')).filter(Q(search=book_name) | Q(search__icontains=book_name))
   
     return render(request, 'search.html',{'data':data})



def CategorySearch(request,pk):
     data=Book.objects.filter(category__title=pk).order_by('date')
     return render(request, 'search.html',{'data':data})



def AuthorSearch(request,pk):
     data=Book.objects.filter(author__name=pk).order_by('date')
     return render(request, 'search.html',{'data':data})

@login_required(login_url='/account/login/')
def BookDetails(request,pk):
     data=Book.objects.get(slug=pk)

     return render(request, 'bookDetails.html',{'data':data})


def index(request):
     if 'book-id' in request.POST:
          bookId=request.POST.get('book-id')
          data=Book.objects.get(id=bookId)
          cartProduct=CartProduct.objects.filter(user=request.user.email)
          product=cartProduct.filter(product=bookId)
          if product:
               messages.error(request,'Book Already Add to cart! Go to cart')
          else:
            
               cart = CartProduct.objects.create(user=request.user.email,product=bookId,book_id=bookId)
               cart.save()
               messages.success(request,'Successfully add to cart')
          return redirect('bookapp:details',pk=data.slug)

@login_required(login_url='/account/login/')
def Cart(request):
     cartProduct=CartProduct.objects.filter(user=request.user.email)
     item=len(cartProduct)
     subtotal=sum(item.total for item in cartProduct)
     totalPrice=subtotal + 5
  
     return render(request, 'cart.html',{'cartProduct': cartProduct,'subtotal':subtotal,'item':item,'totalPrice':totalPrice})



def increaseItem(request,pk):
     cartProduct=CartProduct.objects.filter(user=request.user.email)
     product=cartProduct.get(product=pk)
     product.quantity +=1
     product.save()
     return redirect('bookapp:cart')


def removeItem(request,pk):
     cartProduct=CartProduct.objects.filter(user=request.user.email)
     product=cartProduct.get(product=pk)
     if product.quantity>1:
          product.quantity -=1
          product.save()
     return redirect('bookapp:cart')


def deleteItem(request,pk):
     cartProduct=CartProduct.objects.filter(user=request.user.email)
     product=cartProduct.get(product=pk)
     product.delete()
     return redirect('bookapp:cart')


@login_required(login_url='/account/login/')
def OrderItem(request):
     cartProduct=CartProduct.objects.filter(user=request.user.email)
     if cartProduct:
          for i in cartProduct:
               order=Order.objects.create(user=request.user.email,book_id=i.book_id,quantity=i.quantity,total=i.total)
               order.save()
          cartProduct.delete()
          messages.success(request,'Order Successfully')
     else:
          messages.error(request,'No Cart To Order!')
     return redirect('bookapp:cart')



def myOrder(request):
     orderProduct= Order.objects.filter(user=request.user.email)
     return render(request, 'myorder.html',{'orderProduct':orderProduct})