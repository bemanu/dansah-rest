from django.contrib import admin

from .models import Role


@admin.register(Role)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("type__startswith",)
    fields = ("type",
              "description",
              "icon_image"
              )
    list_display = ("type",
                    "description",
                    "icon_image_path",
                    "created_at",

                    )
    list_filter = ("type",
                   "description",
                   "created_at",
                   )
