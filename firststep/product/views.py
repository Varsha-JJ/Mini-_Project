from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Product,Category,Size,Cart,Filter_Price
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from logapp.models import Account

# Create your views here.
def product_detail(request,id):
    sizes = Size.objects.all()
    wishlist = Wishlist.object.filter(Q(product=product) & Q(user=request.user))
    products = Product.objects.get(id=id)
    cart = Cart.objects.all()
    return render(request,'product.html',{'product' : products,'size':sizes,'cart':cart})

# def category(request):
#     return render(request,'category.html')

def category(request,id):
    if( Category.objects.filter(id=id)):
        products   = Product.objects.filter(category_id=id)
    return render(request,'category.html',{'data':category,'product':products})


def shop(request):
    totalitem = 0
    if request.user.is_authenticated :
        totalitem = len(Cart.objects.filter(user = request.user))
    category = Category.objects.all()
    products = Product.objects.all()
    page = Paginator(products,3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    cart = Cart.objects.all()
    filterprice = Filter_Price.objects.all()
    catid = request.GET.get('id')
    if catid:
        products = Product.objects.filter(category_id=catid)
    else:
        products = Product.objects.all()


    return render(request,'shop.html',{'page':page,'data':category,'price':filterprice})   

def girls(request,id):
    products = Product.objects.get(pk=id)
    return render(request,'girls.html',{'product':products}) 


def boys(request):
    return render(request,'boys.html') 
    

# def girls(request,category_id):
#     products = Product.objects.get(id=category_id)
#     return render(request,'girls.html',{'product':products}) 

#        


def wishlist(request):
    return render(request,'wishlist.html')  

def checkout(request):
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    total=0
    for i in cart:
        total += i.product.price * i.product_qty
    category=Category.objects.all()
    return render(request,'checkout.html',{'cart':cart,'total':total,'category':category})   


def girls(request,id):
    return render(request,'girls.html')           

def sample(request):
    return render(request,'sample.html')    

def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(price__icontains=query) | Q(description__icontains=query))
            products = Product.objects.filter(multiple_q) 
            return render(request, 'searchbar.html', {'product':products})
        else:
            messages.info(request, 'No Search Result!!!')
            print("No information to show")
    return render(request, 'searchbar.html', {}) 



#Add to Cart.
@login_required(login_url='login')
def addcart(request,id):
      user = request.user
      item=Product.objects.get(id=id)
      if item.stock>0:
        if Cart.objects.filter(user_id=user,product_id=item).exists():
            return redirect(cart)
        else:
            product_qty=1
            price=item.price * product_qty
            new_cart=Cart(user_id=user.id,product_id=item.id,product_qty=product_qty,price=price)
            new_cart.save()
            return redirect(cart)



# Cart Quentity Plus Settings
def plusqty(request,id):
    cart=Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product.stock > cart.product_qty:
            cart.product_qty +=1
            cart.price=cart.product_qty * cart.product.price
            cart.save()
            return redirect('cart')
        # messages.success(request, 'Out of Stock')
        return redirect('cart')

# Cart Quentity Plus Settings
def minusqty(request,id):
    cart=Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product_qty > 1 :
            cart.product_qty -=1
            cart.price=cart.product_qty * cart.product.price
            cart.save()
            return redirect('cart')
        return redirect('cart')



# View Cart Page
@login_required(login_url='login')
def cart(request):
    # totalitem = 0
    # if request.user.is_authenticated :
    #     totalitem = len(Cart.objects.filter(user = request.user))
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    total=0
    for i in cart:
        total += i.product.price * i.product_qty
    category=Category.objects.all()
    # subcategory=Subcategory.objects.all()
    return render(request,'cart.html',{'cart':cart,'total':total,'category':category})

# Remove Items From Cart
def de_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect(cart)




@login_required(login_url='login')
def checkout_update(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        address = request.POST.get('addres')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        district = request.POST.get('district')
        pincode = request.POST.get('pincode')
        password = request.POST.get('password')
        user_id = request.user.id

        user = Account.objects.get(id=user_id)
        user.first_name = fname
        user.last_name = lname
        user.address = address
        user.email = email
        user.contact = phone
        user.city = city
        user.state = district
        user.pincode = pincode


        if password != None and password != "":
            user.set_password(password)
        user.save()
        messages.success(request,'Profile Updated Successfully')
        return redirect('cart')