import uuid
from django.db import models
from .contactuploadfiles import contact_upload_image_path


class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    address = models.CharField("Address", max_length=255)
    phone_number = models.CharField(max_length=12)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name = "Location"
        verbose_name_plural = "Locations"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"


class Contact(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    locations = models.ManyToManyField(Location)
    cover_image_path = models.ImageField(
        "Cover Image", upload_to=contact_upload_image_path, null=True, blank=True
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"
