from django.contrib import admin

from .models import Course, LeadershipInstitute


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title", "level", "cover_image_path")
    list_display = ("title", "level", "created_at")
    list_filter = ("title", "created_at")


@admin.register(LeadershipInstitute)
class LeadershipInstituteAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("courses",)
    fields = (
        "title",
        "short_description",
        "full_description",
        "action_text",
        "cover_image_path",
        "courses",
    )
    list_display = (
        "title",
        "short_description",
        "cover_image_path",
        "created_at",
    )
    list_filter = (
        "title",
        "created_at",
    )
