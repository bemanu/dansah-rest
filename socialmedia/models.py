import uuid

from django.db import models

from .socialmediauploadfiles import social_media_upload_image_path


class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Social media title", max_length=255)
    logo_image_path = models.ImageField(
        "Logo", upload_to=social_media_upload_image_path, null=True, blank=True
    )
    link = models.CharField(max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")

    def __unicode__(self):
        return "%s: /n  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Tile", max_length=255)
    description = models.TextField("Description", max_length=1024)
    cover_image_path = models.ImageField(
        "Cover Image", upload_to=social_media_upload_image_path, null=True, blank=True
    )
    social_media = models.ManyToManyField(to=SocialMedia)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __unicode__(self):
        return "%s: /n %s %s  %s %s" % (
            self.title,
            self.description,
            self.created_at,
        )

    def __str__(self):
        return f"{self.title}"
