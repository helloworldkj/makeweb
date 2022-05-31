from django.urls import path
from . import views
#from myweb import views 지금 myweb의 위치에 있으므로 위에처럼 쓰기


#myweb앱의 urls.py파일
app_name= "myweb" #django.urls.exceptions.NoReverseMatch: 'myweb' is not a registered namespace
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
]