from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return HttpResponse("<h1>Trang chủ</h1><a href='/hello/'>Hello</a> | <a href='/template/'>Template</a>")

def hello(request):
    return HttpResponse("<h1>Xin chào từ Django!</h1><a href='/'>Về trang chủ</a>")

def hello_template(request):
    return render(request, 'hello.html', {'message': 'Xin chào từ Django Template!'})