from django.contrib import admin

from .models import Activities, HomeActivities


@admin.register(HomeActivities)
class HomeActivitiesAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "sub_title",
              "text",
              "background_image_path",
              "icon_image_path",
              "activities"
              )
    list_display = ("title",
                    "sub_title",
                    "text",
                    "background_image_path",
                    "icon_image_path",
                    "created_at",
                    )
    list_filter = ("title",
                   "sub_title",
                   "text")


@admin.register(Activities)
class ActivitiesAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "alias_title",
              "icon_image",
              )
    list_display = ("title",
                    "alias_title",
                    "icon_image_path")
    list_filter = ("title", "alias_title")
