import uuid
from django.db import models

from .homeministriesmaterialuploadfiles import home_ministries_material_upload_image_path


class MinistriesMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Ministries material title", max_length=255)
    description = models.CharField("Description", max_length=1024)
    image_path = models.ImageField("Icon image", upload_to=home_ministries_material_upload_image_path, null=True, blank=True)
    redirect_link = models.CharField(max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "description", "created_at")

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.title, self.description, self.created_at)

    def __str__(self):
        return f"{self.title}"

class HomeMinistriesMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Intro tile", max_length=255)
    sub_title = models.CharField("Sub-title", max_length=255)
    text = models.TextField("Text", max_length=1024)
    icon_image = models.ImageField("Icon image", upload_to=home_ministries_material_upload_image_path, null=True, blank=True)
    icon_image_path = models.CharField(home_ministries_material_upload_image_path, max_length=255)
    ministries_material = models.ManyToManyField(MinistriesMaterial)
    created_at = models.DateTimeField("Created at", auto_now_add=True)


    class Meta:
        ordering = ("title", "sub_title", "created_at")
        verbose_name = "Home Ministry Material"
        verbose_name_plural = "Home Ministries Materials"

    def __unicode__(self):
        return u'%s: /n %s  %s %s' % (self.title, self.sub_title, self.text, self.created_at)

    def __str__(self):
        return f"{self.title} - {self.sub_title}"