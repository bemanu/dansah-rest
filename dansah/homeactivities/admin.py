from django.contrib import admin

from .models import Activitie, HomeActivitie


@admin.register(HomeActivitie)
class HomeActivitiesAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    inline = (Activitie,)
    filter_horizontal = ('activities',)
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


@admin.register(Activitie)
class ActivitiesAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "alias_title",
              "icon_image_path",


              )
    list_display = ("title",
                    "alias_title",
                    "icon_image_path",

                    )
    list_filter = ("title",
                   "alias_title"
                   )

