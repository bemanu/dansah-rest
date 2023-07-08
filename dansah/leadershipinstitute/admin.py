from django.contrib import admin

from .models import Course, Category, LeadershipInstitute


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "level",
        "short_description",
        "full_description",
        "cover_image_path",
    )
    list_display = ("name", "level", "created_at")
    list_filter = ("name", "created_at")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ("name__startswith",)
    fields = (
        "name",
        "cover_image_path",
    )
    list_display = ("name", "created_at")
    list_filter = ("name", "created_at")


@admin.register(LeadershipInstitute)
class LeadershipInstituteAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ("categories",)
    fields = (
        "title",
        "short_description",
        "full_description",
        "action_text",
        "cover_image_path",
        "categories",
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
