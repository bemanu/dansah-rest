from django.contrib import admin

from .models import Devotional


@admin.register(Devotional)
class DevotionalAdmin(admin.ModelAdmin):
    search_fields = ("devotion_title__startswith",)
    fields = ("devotion_title", "devotion_message", "devotion_date", "devotion_monthly")
    list_display = ("devotion_title", "devotion_message", "devotion_date", )
    list_filter = ("devotion_created_at", "devotion_monthly","devotion_monthly")

