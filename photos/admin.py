from django.contrib import admin

from photos.models import Photo


# Register your models here.
@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "date_of_publication", "description", "get_tagged_pets")

    @staticmethod
    def get_tagged_pets(photo):
        return ", ".join([pet.name for pet in photo.tagged_pets.all()])