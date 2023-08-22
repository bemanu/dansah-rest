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
    fields = ("title", "description", "cover_image_path")
    list_display = (
        "title",
        "created_at",
    )
    list_filter = ("title", "description", "created_at")
