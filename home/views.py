from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
# Create your views here.

def index(request):
    context = {
        'variable': 'Hello World'
    }
    return render(request,'index.html',context)
    #return HttpResponse("Hello world")

def about(request):
    return render(request, 'about.html')
    #return HttpResponse("Hello about")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.now())
        contact.save()
        messages.success(request, "Thank you for contacting me!")
    return render(request, 'contact.html' )
    #return HttpResponse("Hello contact")

def services(request):
    return render(request, 'services.html')
    #return HttpResponse("Hello services")
