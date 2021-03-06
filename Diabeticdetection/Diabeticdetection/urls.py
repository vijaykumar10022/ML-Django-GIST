"""Diabeticdetection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from diabetic import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',views.signup),
    path('static1/',views.static1),
    path('dynamic1/<str:name>/<int:age>/<str:place>/',views.dynamic1),
    path('dynamic2/<str:name>/<int:age>/',views.dynamic2),
    path('details/<str:name>/<str:place>',views.details),
    path('add/<int:v1>/<int:v2>/',views.add),
    path('demo/',views.demo),
    path('data/',views.data),
    path('data2/<int:roll>/<str:name>/',views.data2),
    path('register/',views.register,name='register'),

]
