from django.contrib import admin

from .models import HomeActivity


@admin.register(HomeActivity)
class HomeActivitiesAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = (
        "title",
        "description",
        "background_image_path",
    )

    list_display = (
        "title",
        "created_at",
    )
    list_filter = ("title",)
