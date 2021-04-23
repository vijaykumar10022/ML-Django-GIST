from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def signup(request):
	return HttpResponse("<h1 style=color:red>Hello This is i am from signup Response,this is vijay</h1>")
def static1(request):
	return HttpResponse("<h1> i am vijay from Vijayawada.</h1>")
def dynamic1(request,name,age,place):
	return HttpResponse("<h2> my name is {} and my age is  i am from {}</h2>".format(name,place))
	# return HttpResponse("<h2> my name is </h2>"+name+"<h2>Age is </h2>"+str(age)+"<h2>place is <h2>"+place)
def details(request,name,place):
	return HttpResponse("<h2> my name is {} and i am from {}</h2>".format(name,place))
def dynamic2(request,name,age):
	return HttpResponse("<h2> my name is {} and   i am from {}</h2>".format(name,age))
def add(request,v1,v2):
	res=v1+v2
	return HttpResponse("<h1>Addition of {} and {} is {} </h1>".format(v1,v2,res))