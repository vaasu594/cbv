# from tkinter import Y
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

class GetInput(View):
    def get(self,request):
        return render(request,'get_input.html')

class PostInput(View):
    def get(self,request):
        return render(request,'post_input.html')

class Add(View):
    def get(self,request):
        try:
            a=int(request.GET['a'])

            b=int(request.GET['b'])

            z=a+b
            return HttpResponse("sum :"+str(z))

        except ValueError:
            return HttpResponse("invalid input")

    def post(self,request):
        if request.method=='POST':
            try:
                a=int(request.POST['f'])

                b=int(request.POST['s'])

                z=a+b
                return HttpResponse("sum :"+str(z))

            except ValueError:
                return HttpResponse("invalid input")

# Create your views here.
