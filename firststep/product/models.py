from django.db import models 
from logapp.models import Account
import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe

# Create your models here.

class Category(models.Model):
    title       = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='category_image/',blank=True,null=True)
    slug        = models.SlugField(max_length=255, unique=True)


    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse('category', args=[self.slug])



class Product(models.Model):
    name          = models.CharField(max_length=100)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    product_image = models.ImageField(upload_to='product_image/')
    price         = models.IntegerField(default=0)
    stock         = models.IntegerField(default=0)
    description   = models.TextField(max_length=1000,default='')
    slug          = models.SlugField(max_length=255,unique=True)
    in_stock      = models.BooleanField(default=True)
    is_active     = models.BooleanField(default=True)
    publish       = models.DateTimeField(default=timezone.now)
    updated       = models.DateTimeField(auto_now=True)
    
    def __str__(self):
       return self.name

    def get_url(self):
        return reverse('product_detail', args=[self.slug]) 


class Color(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20,blank=True,null=True)
       
    def __str__(self):
       return self.name 

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p> style="background-color:{}">Color</p>'.format(self.code))

class Size(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
       return self.name


class Filter_Price(models.Model):
    Filter_Price = (
        ('0 to 250','0 TO 250'),
        ('250 TO 500','250 TO 500'),
        ('500 TO 1000','500 TO 1000'),
        ('1000 TO 2000','1000 TO 2000')
    )

    price = models.CharField(choices=Filter_Price,max_length=65)



class Cart(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(default=1)
    price=models.DecimalField(max_digits=20,decimal_places=2,default=0)

    def get_product_price(self):
        price=[self.product.price]
        return sum(price)
    


class Wishlist(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)