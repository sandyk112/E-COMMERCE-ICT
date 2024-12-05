from django.contrib import admin
from django.urls import path
from my_app import views  # Import the views from my_app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),  # Add the index view here
    path('contact-us/',views.contact,name='contact'),
    path('about-us/',views.about,name='about'),
    path('register/',views.register,name='register'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('beauty-care/',views.beautycare,name='beautycare'),
    path('grocery/',views.grocery,name='grocery'), 
    path('home-kitchen/',views.homekitchen,name='grocery'), 
    path('kid/',views.kid,name='grocery'),
    path('kid-details/',views.kiddetails,name='grocery'),
    path('men/',views.men,name='grocery') ,
    path('personal-care/',views.personalcare,name='grocery'),
    # Add the index view here
]
