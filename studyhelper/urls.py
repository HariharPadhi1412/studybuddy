from django.http import HttpResponse
from django.contrib import admin
from django.urls import path,include

def home(request):
    return HttpResponse("hello world")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('base.urls')),
]
