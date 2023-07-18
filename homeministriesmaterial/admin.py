from django.contrib import admin

from .models import MinistriesMaterial, HomeMinistriesMaterial


@admin.register(HomeMinistriesMaterial)
class HomeMinistriesMaterialAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("materials",)
    fields = (
        "title",
        "materials",
    )
    list_display = (
        "title",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )


@admin.register(MinistriesMaterial)
class MinistriesMaterialAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "description", "cover_image_path", "redirect_link")
    list_display = (
        "title",
        "description",
        "cover_image_path",
        "redirect_link",
        "created_at",
    )
    list_filter = ("title", "created_at")
