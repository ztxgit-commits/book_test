from django.contrib import admin
from django.urls import path,include
from book_app import views

urlpatterns = [
    path('/login',views.login),

]
