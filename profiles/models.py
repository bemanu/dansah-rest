import uuid

from django.db import models


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    type = models.CharField("Type", max_length=255)
    description = models.CharField("Description", max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("type", "description", "created_at")
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.type, self.description, self.created_at)

    def __str__(self):
        return f"{self.type}"


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255, default="Profile")
    text = models.TextField("Text", max_length=1024)
    roles = models.ManyToManyField(Role)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "text")
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"{self.title}"
