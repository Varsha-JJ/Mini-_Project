from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Product,Category,Size,Cart
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from logapp.models import Account

# Create your views here.
def product_detail(request,slug_product):
    sizes = Size.objects.all()
    products = Product.objects.get(slug=slug_product)
    return render(request,'product.html',{'product' : products,'size':sizes})

# def category(request):
#     return render(request,'category.html')

def category(request,slug):
    category = Category.objects.get(slug=slug)
    context = {'category':category}
    return render(request,'category.html',context)

@login_required(login_url='login')
def shop(request):
    category = Category.objects.all()
    products = Product.objects.all()
    page = Paginator(products,3)
    page_list = request.GET.get('page')
    page = page.get_page(page_list)
    return render(request,'shop.html',{'page':page,'data':category})   

def girls(request,id):
    products = Product.objects.get(pk=id)
    return render(request,'girls.html',{'product':products}) 


def boys(request):
    return render(request,'boys.html') 
    

# def girls(request,category_id):
#     products = Product.objects.get(id=category_id)
#     return render(request,'girls.html',{'product':products}) 

def cart(request):
    return render(request,'cart.html')        


def wishlist(request):
    return render(request,'wishlist.html')  

def checkout(request):
    return render(request,'checkout.html')   

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
                  price=item.selling_price * product_qty
                  new_cart=Cart(user_id=user.id,product_id=item.id,product_qty=product_qty,price=price)
                  new_cart.save()
                  return redirect(cart)



# Cart Quentity Plus Settings
def plusqty(request,id):
    cart=Cart.objects.filter(id=id)
    for cart in cart:
        if cart.product.stock > cart.product_qty:
            cart.product_qty +=1
            cart.price=cart.product_qty * cart.product.selling_price
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
            cart.price=cart.product_qty * cart.product.selling_price
            cart.save()
            return redirect('cart')
        return redirect('cart')



# View Cart Page
@login_required(login_url='login')
def cart(request):
    user = request.user
    cart=Cart.objects.filter(user_id=user)
    total=0
    for i in cart:
        total += i.product.selling_price * i.product_qty
    category=Category.objects.all()
    # subcategory=Subcategory.objects.all()
    return render(request,'cart.html',{'cart':cart,'total':total,'category':category})

# Remove Items From Cart
def de_cart(request,id):
    Cart.objects.get(id=id).delete()
    return redirect(cart)
