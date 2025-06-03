from django.shortcuts import render

# Create your views here.

# the html files are present in the templates folder of this app 
def shop_finder(request):
    return render(request,'shop_finder.html')

 
