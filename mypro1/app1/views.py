from django.shortcuts import render, HttpResponse,redirect
from .forms import StudentForm

# Create your views here.
# def home(request):
#      v="This is Home page"
#      return render(request, 'home.html',{'data':v})

# def register(request):
#      return render(request, 'register.html')

def login(request):
     l="This is Login page"
     return render(request, 'login.html',{'data':l})

def logout(request):
     return render(request, 'logout.html')

def register(request):
     st=StudentForm()
     if request.method=='POST':
          s=StudentForm(request.POST)
          if s.is_valid():
               s.save()
               # return HttpResponse("<h1>Form submitted</h1>")
               return redirect('login')
     return render(request, 'register.html',{'form':st})

from django.shortcuts import render
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})
