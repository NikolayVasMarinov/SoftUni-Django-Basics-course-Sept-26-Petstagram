from django.urls import path, include
import views

app_name = "photos"
urlpatterns = [
    path("add/", views.add_photo, name="photo-add"),
    path("<int:pk>/", include([
        path("", views.photo_details, name="photo-details"),
        path("edit/", views.edit_photo, name="photo-edit"),
    ])),
]