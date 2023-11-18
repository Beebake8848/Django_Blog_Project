from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def dashboard(request):
    return render(request, 'blog/dashboard.html')

def signup(request):
    return render(request, 'blog/signup.html')

def login(request):
    return render(request, 'blog/login.html')

def logout(request):
    return render(request, 'blog/logout.html')