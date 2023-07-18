from django.contrib import admin

from .models import Media, SocialMedia


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("social_media",)
    fields = (
        "title",
        "description",
        "cover_image_path",
        "social_media",
    )
    list_display = (
        "title",
        "description",
        "cover_image_path",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "logo_image_path", "link")
    list_display = (
        "title",
        "logo_image_path",
        "link",
        "created_at",
    )
    list_filter = ("title", "created_at")
