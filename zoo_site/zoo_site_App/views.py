from django.shortcuts import render

def home(request):
    return render(request,'zoo.html')

def animals(request):
    return render(request,'animals.html')

def tickets(request):
    return render(request,'tickets.html')

def thankyou(request):
    return render(request,'thankyou.html')

def instructions(request):
    return render(request,'instructions.html')
