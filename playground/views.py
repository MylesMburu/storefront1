# Create your views here.
# this is an event handler
# it recieves requests and gives out responses

from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # can pull data from a database
    # send an email
    # return HttpResponse('Hello world')

    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Mbush'})
