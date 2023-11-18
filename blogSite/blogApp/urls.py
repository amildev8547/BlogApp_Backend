from django.urls import path
from . import views

urlpatterns = [
    path('viewAll', views.viewAllPost, name='viewAll'),
    path('viewMy', views.viewMyPost, name='viewMy'),
    path('addBlog', views.addBlog, name='addBlog'),
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    
]
