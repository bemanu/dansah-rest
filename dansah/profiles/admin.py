from django.contrib import admin

from .models import Profiles


@admin.register(Profiles)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "sub_title",
              "text",
              "roles"
             )
    list_display = ("title",
                    "sub_title",
                    "text",
                    "roles",
                    "created_at"

                    )
    list_filter = ("title",
                   "roles",
                   "created_at"
                   )
