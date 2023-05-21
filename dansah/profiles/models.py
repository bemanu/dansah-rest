import uuid

from django.db import models


class Profiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Intro tile", max_length=255)
    sub_title = models.CharField("Sub tile", max_length=255)
    text = models.CharField("Intro text", max_length=1024)
    roles = models.CharField("Intro text", max_length=1024)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

