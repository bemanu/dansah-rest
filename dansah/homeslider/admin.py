from django.contrib import admin

from .models import HomeSlider, Intro


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "image1", "image2", "image3")
    list_display = ("title", "image1", "image2", "image3", "created_at")
    list_filter = ("title", "created_at")


@admin.register(Intro)
class IntroAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "sub_title", "text", "image_path", "icon_image_path")
    list_display = (
        "title",
        "sub_title",
        "text",
        "image_path",
        "icon_image_path",
        "created_at",
    )
    list_filter = ("title", "sub_title", "created_at")
