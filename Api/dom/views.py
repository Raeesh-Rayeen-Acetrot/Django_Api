from django.shortcuts import render

# Create your views here.
def myfun(request):
    return render(request,'index.html')


def mydata(request):
    return render(request,'index.html')