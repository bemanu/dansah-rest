import uuid
from django.db import models

from .prayercityuploadfiles import prayer_city_upload_image_path


# Create your models here.
class PrayerCity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    sub_title = models.DateTimeField("Subtitle", auto_now_add=True)
    short_description = models.CharField("Short Description", max_length=255)
    full_description = models.TextField(
        "Full Description", max_length=1024, blank=False
    )
    cover_image_path = models.ImageField(
        "Cover image", upload_to=prayer_city_upload_image_path, null=True, blank=True
    )
    action_text = models.CharField("Action Text", max_length=255, blank=True)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name_plural = "Prayer City"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"
