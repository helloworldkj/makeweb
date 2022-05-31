#from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#from .models import Post #만든 모델 불러오기

def index(request):
    #return HttpResponse("hello hoho") #단순히 글자를 response로 보내기
    return render(request,'myweb/index.html') #html을 리턴해주기

def home(request):
    return render(request, 'myweb/home.html') #로그인 후 home return