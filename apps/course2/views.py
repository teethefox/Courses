from django.shortcuts import render, redirect
from django.contrib.messages import error

from models import *

def index(request):
    Course.objects.all()
    context={
        "courses":Course.objects.all()

    }

    return render(request,'index.html',context)
def add(request):

    return render(request,'add.html')
def create(request):
    errors = Course.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:

        Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/')
def delete(request,id):
    bill=Course.objects.get(id=id)
    bill.delete()
    return redirect('/')
def um(request, id):
    Course.objects.all()
    context={
        "course":Course.objects.get(id=id)

    }

    return render(request,'um.html', context)
# Create your views here.
