import uuid
from django.db import models

from .homeactivitiesuploadfiles import home_activities_upload_image_path


class HomeActivity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    description = models.TextField("Description", max_length=1024, blank=False)
    background_image_path = models.ImageField(
        "Background image",
        upload_to=home_activities_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title",)
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"
