from django.shortcuts import render

# Create your views here.

def student(request):
    return render(request,'student.html')

def lect(request):
    return render(request,'lect.html')

def student2(request):
    return render(request,'student2.html')

def student3(request):
    return render(request,'student3.html')

def lect2(request):
    return render(request,'lect2.html')

def lect3(request):
    return render(request,'lect3.html')