import uuid
from django.db import models
from .leadershipInstitueuploadfiles import (
    leadership_institute_upload_image_path,
    leadership_institute_course_upload_image_path,
    leadership_institute_categories_upload_image_path,
)


LEVELS = (
    ("BASIC", "Basic"),
    ("INTERMEDIATE", "Intermediate"),
    ("ADVANCED", "Advanced"),
)


class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    level = models.ForeignKey("Category", on_delete=models.CASCADE, blank=False)
    short_description = models.CharField(
        "Short Description", max_length=255, default="", blank=False
    )
    full_description = models.TextField(
        "Full Description", max_length=1024, default="", blank=False
    )
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=leadership_institute_course_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Courses"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Name", max_length=255)
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=leadership_institute_categories_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("name", "created_at")
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.name, self.created_at)

    def __str__(self):
        return f"{self.name}"


class LeadershipInstitute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Title", max_length=255)
    sub_title = models.DateTimeField("Subtitle", auto_now_add=True)
    short_description = models.CharField("Short Description", max_length=255)
    full_description = models.TextField(
        "Full Description", max_length=1024, blank=False
    )
    categories = models.ManyToManyField(Category)
    action_text = models.CharField("Action Text", max_length=255, blank=True)
    cover_image_path = models.ImageField(
        "Cover image",
        upload_to=leadership_institute_upload_image_path,
        null=True,
        blank=True,
    )
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")
        verbose_name_plural = "Leadership Institute"

    def __unicode__(self):
        return "%s: /n %s  %s" % (self.title, self.created_at)

    def __str__(self):
        return f"{self.title}"
