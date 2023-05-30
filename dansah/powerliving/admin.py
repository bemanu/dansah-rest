from django.contrib import admin

from .models import PowerLiving, MonthlyPowerLiving


@admin.register(PowerLiving)
class PowerLivingAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    filter_horizontal = ('monthly_power_living',)
    fields = ("title",
              "sub_title",
              "Icon_image",
              "monthly_power_living",
              )
    list_display = ("title",
                    "sub_title",
                    "Icon_image",
                    "created_at",

                    )
    list_filter = ("title",
                   "sub_title",
                   "created_at"
                   )


@admin.register(MonthlyPowerLiving)
class MonthlyPowerLivingAdmin(admin.ModelAdmin):
    search_fields = ("title__startswith",)
    fields = ("title",
              "cover_image_path",
              )
    list_display = ("title",
                    "cover_image_path",
                    "created_at",

                    )
    list_filter = ("title",
                   "created_at",
                   )
