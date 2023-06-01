import uuid
from django.db import models

from .homeactivitiesuploadfiles import home_activities_upload_image_path


class HomeActivitie:
    pass


class Activitie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Activity tile", max_length=255)
    alias_title = models.CharField("Sub tile", max_length=255)
    icon_image_path = models.ImageField("Icon image", upload_to=home_activities_upload_image_path, null=True, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "alias_title")
        verbose_name = "Activity"
        verbose_name_plural = "Activities"

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.title, self.alias_title, self.created_at)

    def __str__(self):
        return f"{self.title} - {self.alias_title}"



class HomeActivitie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Home activity tile", max_length=255)
    sub_title = models.CharField("Sub tile", max_length=255)
    text = models.TextField("Text", max_length=1024)
    background_image_path = models.ImageField("Background image", upload_to=home_activities_upload_image_path, null=True, blank=True)
    icon_image_path = models.ImageField("Icon image", upload_to=home_activities_upload_image_path, null=True, blank=True)
    activities = models.ManyToManyField(Activitie)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        db_table = "homeactivities"
        ordering = ("title", "sub_title", "created_at")

    def __unicode__(self):
        return u'%s: /n %s  %s %s' % (self.title, self.sub_title, self.text, self.created_at)

    def __str__(self):
        return f"{self.title}"
