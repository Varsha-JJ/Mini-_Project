from django.urls import path
from . import views

urlpatterns = [
    path('product_detail/<slug:slug_product>/',views.product_detail,name='product_detail'),
    path('shop/',views.shop,name='shop'),
    path('cart/',views.cart,name='cart'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('girls/',views.girls,name='girls'),
    path('checkout/',views.checkout,name='checkout'),
    path('category/',views.category,name='category'),
    path('searchbar/',views.searchbar,name='searchbar'),
    path('<int:id>',views.girls,name='girls'),
    path('boys/',views.boys,name='boys'),
    path('addcart/<int:id>/', views.addcart, name='addcart'),
    path('de_cart/<int:id>/', views.de_cart, name='de_cart'),
    path('plusqty/<int:id>/',views.plusqty,name='plusqty'),
    path('minusqty/<int:id>/',views.minusqty,name='minusqty'),
    
]
