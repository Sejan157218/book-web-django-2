from django.db import models
import datetime
from django.utils.translation import gettext as _
# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.title


class Author(models.Model):
    name=models.CharField(max_length=300)
    image =models.ImageField(upload_to="authors/")
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.name


class Publisher(models.Model):
    name=models.CharField(max_length=300)
    image =models.ImageField(upload_to="publisher/")
    description=models.TextField(max_length=300)
    date=models.DateField(auto_now_add=True)
    def __str__(self) :
        return self.name


YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]
class Book(models.Model):
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,blank=True,null=True)
    publisher=models.ForeignKey(Publisher,on_delete=models.SET_NULL,blank=True,null=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,blank=True,null=True)
    title=models.CharField(max_length=200)
    slug=models.SlugField(max_length=200,blank=True)
    date=models.DateField(auto_now_add=True)
    market_price=models.PositiveBigIntegerField()
    discount_percent  = models.FloatField(null=True, blank=True)
    description=models.TextField()
    edition_number=models.CharField(max_length=10,default=None)
    edition_year = models.IntegerField(_('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    stock=models.IntegerField(default=None)
    image =models.ImageField(upload_to="book/")


    def snippet(self):
        return self.category.title


    @property
    def discount(self):
        if not self.discount_percent is None and self.discount_percent  > 0:
            discounted_price = self.market_price - self.market_price * self.discount_percent  / 100
            return round(discounted_price, 2)



    @property
    def categoryTitle(self):
        return self.category.title
        
    @property
    def authorName(self):
        return self.author.name


    @property
    def publisherName(self):
        return self.publisher.name


    def __str__(self):
        return self.title
