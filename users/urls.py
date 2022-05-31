from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

#users앱의 urls.py파일
app_name="users"
urlpatterns=[
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup')
]