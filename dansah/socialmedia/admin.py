from django.contrib import admin

from .models import Media, SocialMedia


@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ('social_media',)
    fields = ("title",
              "sub_title",
              "paragraph_title",
              "description_1",
              "description_2",
              "image",
              "social_media",
              )
    list_display = ("title",
                    "sub_title",
                    "paragraph_title",
                    "description_1",
                    "description_2",
                    "image",
                    "created_at",
                    )
    list_filter = ("title",
                   "created_at",
                   )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "icon_name",
              "image_path",
              "redirect_link"
              )
    list_display = ("title",
                    "icon_name",
                    "image_path",
                    "redirect_link",
                    "created_at",
                    )
    list_filter = ("title",
                   "created_at"
                   )
