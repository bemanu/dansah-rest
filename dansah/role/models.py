import uuid
from django.db import models

from .uploadfiles import upload_image_path


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField("Role type", max_length=255)
    description = models.CharField("Role description", max_length=255)
    icon_image_path = models.ImageField("Icon", upload_to=upload_image_path, null=True, blank=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("type", "description", "created_at")
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __unicode__(self):
        return u'%s: /n %s  %s' % (self.type, self.description, self.created_at)

    def __str__(self):
        return f"{self.type}"