import uuid
from django.db import models

from .homeeventsuploadfiles import home_events_upload_image_path


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Ministries material title", max_length=255)
    description = models.CharField("Description", max_length=1024)
    icon_image_path = models.ImageField("Icon image", upload_to=home_events_upload_image_path, null=True, blank=True)
    date_detail_1 = models.CharField("Date details", max_length=255)
    date_detail_2 = models.CharField("Date details 2", max_length=255)
    created_at = models.DateField("Created at", auto_now_add=True)


    class Meta:
        ordering = ("title", "description", "created_at")
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.title, self.description, self.created_at)

    def __str__(self):
        return f"{self.title}"

class HomeEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Intro tile", max_length=255)
    sub_title = models.CharField("Sub tile", max_length=255)
    icon_image_path = models.ImageField("Icon image", upload_to=home_events_upload_image_path, null=True, blank=True)
    events = models.ManyToManyField(to=Event)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "sub_title", "created_at")
        verbose_name = "Home Event"
        verbose_name_plural = "Home Events"

    def __unicode__(self):
        return u'%s: /n %s  %s ' % (self.title, self.sub_title, self.created_at)

    def __str__(self):
        return f"{self.title}"