from django.urls import path
from . import views

urlpatterns = [
    path('product_detail/<int:id>/',views.product_detail,name='product_detail'),
    path('shop/',views.shop,name='shop'),
    path('cart/',views.cart,name='cart'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('girls/',views.girls,name='girls'),
    path('size/<int:id>',views.size,name='size'),
    path('color/<int:id>',views.color,name='color'),
    path('price/<int:id>',views.price,name='price'),
    path('checkout/',views.checkout,name='checkout'),
    path('category/<int:id>/',views.category,name='category'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('girls/',views.girls,name='girls'),
    path('boys/',views.boys,name='boys'),
    path('addcart/<int:id>/', views.addcart, name='addcart'),
    path('de_cart/<int:id>/', views.de_cart, name='de_cart'),
    path('plusqty/<int:id>/',views.plusqty,name='plusqty'),
    path('minusqty/<int:id>/',views.minusqty,name='minusqty'),
    path('orders/', views.shop, name='orders'),
    path('checkout_update/',views.checkout_update,name='checkout_update'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('add_wishlist/<int:id>/',views.add_wishlist,name='add_wishlist'),
    path('view_wishlist',views.view_wishlist,name='view_wishlist'),
    path('de_wishlist/<int:id>/',views.de_wishlist,name='de_wishlist'),
]
