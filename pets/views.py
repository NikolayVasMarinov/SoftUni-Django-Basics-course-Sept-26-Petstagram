from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def add_pet(request: HttpRequest) -> HttpResponse:
    return render(request, "pets/pet-add-page.html")

def pet_details(request: HttpRequest) -> HttpResponse:
    return render(request, "pets/pet-details-page.html")

def edit_pet(request: HttpRequest) -> HttpResponse:
    return render(request, "pets/pet-edit-page.html")

def delete_pet(request: HttpRequest) -> HttpResponse:
    return render(request, "pets/pet-delete-page.html")
