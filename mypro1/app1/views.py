from django.shortcuts import render

# Create your views here.

def home(request):
     v="This is Home page"
     return render(request, 'home.html',{'data':v})

def register(request):
     return render(request, 'register.html')

def login(request):
     l="This is Login page"
     return render(request, 'login.html',{'data':l})

def logout(request):
     return render(request, 'logout.html')
