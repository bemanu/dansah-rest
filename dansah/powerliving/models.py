import uuid
from django.db import models

from .powerlivinguploadfiles import power_living_upload_image_path


class MonthlyPowerLiving(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Monthly Power Living tile", max_length=255)
    cover_image_path = models.ImageField("Cover image", upload_to=power_living_upload_image_path, null=True, blank=True)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name = "Monthly Power Living"
        verbose_name_plural = "Monthly Power Living"

    def __unicode__(self):
        return u'%s: /n %s ' % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"


class PowerLiving(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Power Living title", max_length=255)
    sub_title = models.CharField("Home slider title", max_length=255)
    Icon_image = models.ImageField("Image", upload_to=power_living_upload_image_path, null=True, blank=True)
    monthly_power_living = models.ManyToManyField(to=MonthlyPowerLiving)
    created_at = models.DateField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "sub_title", "created_at")
        verbose_name = "Power Living"
        verbose_name_plural = "Power Living"

    def __unicode__(self):
        return u'%s: /n %s' % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title} - {self.sub_title}"
