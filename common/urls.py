from django.urls import path
import views

app_name = "common"
urlpatterns = [
    path("", views.home_page, name="home-page"),
]