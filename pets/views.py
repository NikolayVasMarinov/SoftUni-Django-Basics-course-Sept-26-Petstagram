from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def add_pet(request: HttpRequest) -> HttpResponse:
    ...

def pet_details(request: HttpRequest) -> HttpResponse:
    ...

def edit_pet(request: HttpRequest) -> HttpResponse:
    ...

def delete_pet(request: HttpRequest) -> HttpResponse:
    ...
