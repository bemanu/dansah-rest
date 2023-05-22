from django.contrib import admin

from .models import Event, HomeEvent


@admin.register(HomeEvent)
class HomeEventsAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "sub_title",
              "icon_image_path"

              )
    list_display = ("title",
                    "sub_title",
                    "icon_image_path",
                    "created_at"

                    )
    list_filter = ("title",
                   "created_at"
                   )


@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "description",
              "icon_image_path",
              "date_detail_1",
              "date_detail_2"
              )
    list_display = ("title",
                    "description",
                    "icon_image_path",
                    "date_detail_1",
                    "date_detail_2",
                    "created_at"
                    )
    list_filter = ("title", "created_at")
