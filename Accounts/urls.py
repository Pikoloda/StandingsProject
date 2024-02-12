from django.urls import path
from . import views
from .views import register, user_login, login_view

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
