from django.http import HttpResponse
from django.shortcuts import render
from . models import Place
from . models import Member

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    cls=Member.objects.all()
    return render(request,"index.html",{'result':obj,'result1':cls})




