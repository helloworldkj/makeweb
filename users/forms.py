#user앱 내의 forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


 #django.contrib.auth.forms의 userCreationForm클래스를 상속해서 UserForm을 만든다.
class UserForm(UserCreationForm):
    email=forms.EmailField(label="이메일") #거기에 이메일 속성을 추가

	#django는 모델을 이용해서 데이터베이스 테이블과 필드 설계
    #모델에 데이터를 추가할 때, Meta클래스 사용
    class Meta: 
        model=User
        fields=("username", "password1","password2","email")