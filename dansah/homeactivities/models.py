import uuid
from django.db import models

from .uploadfiles import upload_image_path


class Activities(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Intro tile", max_length=255)
    alias_title = models.CharField("Sub tile", max_length=255)
    icon_image = models.ImageField("Icon image", upload_to=upload_image_path, null=True, blank=True)
    icon_image_path = models.CharField(max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)


    class Meta:
        ordering = ("title", "alias_title")

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.title, self.alias_title, self.created_at)


class HomeActivities(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Intro tile", max_length=255)
    sub_title = models.CharField("Sub tile", max_length=255)
    text = models.CharField("Intro text", max_length=1024)
    background_image_path = models.ImageField("Background image", upload_to=upload_image_path, null=True, blank=True)
    icon_image_path = models.ImageField("Icon image", upload_to=upload_image_path, null=True, blank=True)
    activities = models.ManyToManyField(Activities)
    created_at = models.DateTimeField("Created at", auto_now_add=True)


    class Meta:
        ordering = ("title", "sub_title", "created_at")

    def __unicode__(self):
        return u'%s: /n %s  %s %s' % (self.title, self.sub_title, self.text, self.created_at)


