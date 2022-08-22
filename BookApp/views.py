from unicodedata import category
from django.http import HttpResponse,JsonResponse
import json
from django.shortcuts import render
from .models import *
from django.contrib.postgres.search import SearchVector,SearchQuery
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def baseData(request):
    category =Category.objects.all();
    author =Author.objects.all();
    return {
        'category':category,
        'authors':author,
    }


def Home(request):
     data =Book.objects.all()
     dramaCategory=Book.objects.filter(category__title="Drama").order_by('date')
     thrillerCategory=Book.objects.filter(category__title="Thriller").order_by('date')
     historyCategory=Book.objects.filter(category__title="History").order_by('date')
     return render(request, 'home.html',{'data':data,'dramaCategory':dramaCategory,'thrillerCategory':thrillerCategory,'historyCategory':historyCategory})


def Cart(request):
     return render(request, 'cart.html')

@login_required(login_url='/account/login/')
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


def AllBook(request):
    # allBook=Book.objects.all()
    # queryset = YourModel.objects.filter(some__filter="some value").values()
    data = list(Book.objects.values())
    return JsonResponse(data,safe=False)
 