from django.shortcuts import render
# from django.http import  HttpResponse
# Create your views here.

def index(request):
    return render(request,'student_list.html')
    # return HttpResponse("Hola soy GOKU! gaaa")
