from django.shortcuts import render

# Create your views here.

# the html files are present in the templates folder of this app 
def landing(request):
    return render(request,'landing.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def about(request):
    return render(request,'about.html')

def forget_password(request):
    return render(request,'forget_password.html')
