from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def add_photo(request: HttpRequest) -> HttpResponse:
    ...

def photo_details(request: HttpRequest) -> HttpResponse:
    ...

def edit_photo(request: HttpRequest) -> HttpResponse:
    ...