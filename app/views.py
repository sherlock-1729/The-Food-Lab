from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    return render(request, 'contact.html')

def product(request):
    return render(request, 'product.html')


