from django.contrib import admin

from .models import QuoteOfTheDay


@admin.register(QuoteOfTheDay)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "sub_title",
              "text",
              "source",
              "icon_image_path",
              "background_icon_image_path",
              )
    list_display = ("title",
                    "sub_title",
                    "text",
                    "icon_image_path",
                    "background_icon_image_path",
                    "created_at"

                    )
    list_filter = ("title",
                   "sub_title",
                   "created_at",
                   )
