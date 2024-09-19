from django.shortcuts import render,HttpResponse
from fun.models import Fun
from datetime import datetime
# Create your views here.

def home(request):
    if request.method == 'POST':
        email_2=request.POST['email_2']
        fun = Fun(email_2=email_2)
        fun.save()
    return render(request,"fun_home.html")
