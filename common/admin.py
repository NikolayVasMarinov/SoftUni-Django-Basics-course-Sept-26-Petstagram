from django.contrib import admin

from common.models import Comment, Like


# Register your models here.
@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ("text", "to_photo")

@admin.register(Like)
class Like(admin.ModelAdmin):
    list_display = ("to_photo",)
