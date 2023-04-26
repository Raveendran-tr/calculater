from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,"form1.html")
def calc(request):
    x=int(request.GET['num1'])
    y = int(request.GET['num2'])
    r1=x+y
    r2=x-y
    r3=x*y
    r4=x/y
    return render(request,"form2.html",{'add':r1,'sub':r2,'mul':r3,'div':r4})