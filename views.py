from django.shortcuts import render,HttpResponse
def home(request):
   # return HttpResponse("Welcome to Salman Portfolio Home page (/)")
    return render(request,'home.html')

def About(request):
    return HttpResponse("This website is for all of you which want to create a best portfolio(About)")

def Projects(request):
    return HttpResponse("Portfolio Project is a time saving website which create your best portfolio in just some minutes(/Projects)")

def Contact(request):
    return HttpResponse("Contact us on +92-3036-255-9966(/Contact)")
# Create your views here.
