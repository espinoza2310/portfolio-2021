from django.shortcuts import render
from portfolioapp.models import Home

# Create your views here.


def home(request):
    home=Home.objects.all()
    #data = {
    #    'home' : home,
    #}
    return render(request,"portfolioapp/home.html", {'home': home})

def blog(request):
    
    return render(request,"portfolioapp/blog.html")

