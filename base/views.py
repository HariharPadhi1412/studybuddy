from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1,"name": "new room"},
    {'id':2,"name": "new room 1"},
    {'id':3,"name": "new room 2"},
    {'id':4,"name": "new room 3"},
]

def home(request):
    context = {'rooms': rooms}
    return render(request,'base/home.html',context)

def room(request,pk):
    room = None

    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room}
    return render(request,'base/room.html',context)