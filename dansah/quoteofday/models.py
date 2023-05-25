import uuid
from django.db import models

from .uploadfiles import upload_image_path


class QuoteOfTheDay(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Intro tile", max_length=255)
    sub_title = models.CharField("Sub tile", max_length=255)
    text = models.TextField("Quote of the day text", max_length=1024)
    icon_image_path = models.ImageField("Icon image",upload_to=upload_image_path, null=True, blank=True)
    background_icon_image_path = models.ImageField("Backgorund image", upload_to=upload_image_path, null=True, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "sub_title", "text", "created_at")
        verbose_name = "Quote of the day"
        verbose_name_plural = "Quotes of the day"

    def __unicode__(self):
        return u'%s: /n %s  %s %s' % (self.title, self.sub_title, self.text, self.created_at)

    def __str__(self):
        return f"{self.title} \n {self.sub_title} \n {self.text}"