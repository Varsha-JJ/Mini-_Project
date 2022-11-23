from django.db import models 
from logapp.models import Account
import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.utils.safestring import mark_safe

# Create your models here.

class Category(models.Model):
    title       = models.CharField(max_length=100,unique=True)
    # category_image = models.ImageField(upload_to='category_image/',blank=True,null=True)
    # slug        = models.SlugField(max_length=255, unique=True)


    def __str__(self):
        return self.title
    
    def get_url(self):
        return reverse('category', args=[self.slug])





class Color(models.Model):
    name = models.CharField(max_length=50,unique=True)
    code = models.CharField(max_length=20,blank=True,null=True)
       
    def __str__(self):
       return self.name 

    def color_tag(self):
        if self.code is not None:
            return mark_safe('<p> style="background-color:{}">Color</p>'.format(self.code))

class Size(models.Model):
    name = models.CharField(max_length=50,unique=True)
    code = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
       return self.name
#   Filter_Price = (
#         ('0 to 250','0 TO 250'),
#         ('250 TO 500','250 TO 500'),
#         ('500 TO 1000','500 TO 1000'),
#         ('1000 TO 2000','1000 TO 2000')
#     )

class Filter_Price(models.Model):
    price = models.CharField(max_length=50,default=0,unique=True)

class Product(models.Model):
    name          = models.CharField(max_length=100,unique=True)
    category      = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    size          = models.ForeignKey(Size, on_delete=models.CASCADE, default=1)
    color         = models.ForeignKey(Color, on_delete=models.CASCADE, default=1)
    filterprice   = models.ForeignKey(Filter_Price, on_delete=models.CASCADE,default=1)
    product_image = models.ImageField(upload_to='product_image/',unique=True)
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


class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    amount = models.FloatField(blank=True,null=True)
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)


class OrderPlaced(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),

    )
    user = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    is_ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_cost(self):
        return self.quantity

    def __str__(self):
        return str(self.user)     