import uuid
from django.db import models

from .uploadfiles import upload_image_path


class HomeSlider(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Home slider title", max_length=255)
    image = models.ImageField("Image", upload_to=upload_image_path, null=True, blank=True)
    image1 = models.ImageField("Image 1", upload_to=upload_image_path, null=True, blank=True)
    image2 = models.ImageField("Image 2", upload_to=upload_image_path, null=True, blank=True)
    image_path = models.CharField("Image", max_length=255)
    image_path_1 = models.CharField("Image 1", max_length=255)
    image_path_2 = models.CharField("Image 2", max_length=255)
    created_at = models.DateField("Created at", auto_now_add=True)
    updated_at = models.DateField("update at")

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Home Slider"
        verbose_name_plural = "Home Sliders"

    def __unicode__(self):
        return u'%s: /n %s' % (self.title, self.created_at)


class Intro(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Intro tile", max_length=255)
    sub_title = models.CharField("Sub tile", max_length=255)
    text = models.CharField("Intro text", max_length=1024)
    image_path = models.ImageField("Image", upload_to=upload_image_path, null=True, blank=True)
    icon_image_path = models.ImageField("Icon", upload_to=upload_image_path, null=True, blank=True)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "sub_title", "text", "created_at")
        verbose_name = "Intro"
        verbose_name_plural = "Intros"

    def __unicode__(self):
        return u'%s: /n %s  %s %s' % (self.title, self.sub_title, self.text, self.created_at)

    def __str__(self):
        return f"{self.title}"