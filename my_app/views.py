from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact-us.html')
def about(request):
    return render(request, 'about-us.html')
def register(request):
    return render(request, 'register.html')
def wishlist(request):
    return render(request, 'wishlist.html')
def checkout(request):
    return render(request, 'checkout.html')
def cart(request):
    return render(request, 'cart.html')
def beautycare(request):
    return render(request, 'beauty-care.html')
def grocery(request):
    return render(request, 'grocery.html')
def homekitchen(request):
    return render(request, 'home-kitchen.html')
def kid(request):
    return render(request, 'kid.html')
def kiddetails(request):
    return render(request, 'kids-details.html')
def men(request):
    return render(request, 'men.html')
def personalcare(request):
    return render(request, 'personal-care.html')
