from django.contrib import admin

from .models import Devotional


@admin.register(Devotional)
class PersonAdmin(admin.ModelAdmin):
    search_fields = ("devotion_title__startswith",)
    fields = ("devotion_title", "devotion_message", "devotion_date", "image")
    list_display = ("devotion_title", "devotion_message", "devotion_date", "image")
    list_filter = ("devotion_created_at", "devotion_monthly")

