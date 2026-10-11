from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def register(request: HttpRequest) -> HttpResponse:
    ...

def login(request: HttpRequest) -> HttpResponse:
    ...

def profile_details(request: HttpRequest) -> HttpResponse:
    ...

def edit_profile(request: HttpRequest) -> HttpResponse:
    ...

def delete_profile(request: HttpRequest) -> HttpResponse:
    ...