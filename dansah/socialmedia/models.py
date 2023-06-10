import uuid

from django.db import models

from .socialmediauploadfiles import social_media_upload_image_path


class SocialMedia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Social media title", max_length=255)
    icon_name = models.CharField("Icon name", max_length=1024)
    image_path = models.ImageField("Icon image", upload_to=social_media_upload_image_path, null=True, blank=True)
    redirect_link = models.CharField(max_length=255)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "created_at")

    def __unicode__(self):
        return u'%s: /n  %s' % (self.title,  self.created_at)

    def __str__(self):
        return f"{self.title}"


class Media(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField("Tile", max_length=255)
    sub_title = models.CharField("Sub-title", max_length=255)
    paragraph_title = models.CharField("Paragraph-title", max_length=255)
    description_1 = models.TextField("Description 1", max_length=1024)
    description_2 = models.TextField("Description 2", max_length=1024)
    image = models.ImageField("Image", upload_to=social_media_upload_image_path, null=True, blank=True)
    social_media = models.ManyToManyField(to=SocialMedia)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        ordering = ("title", "sub_title", "created_at")
        verbose_name = "Media"
        verbose_name_plural = "Media"

    def __unicode__(self):
        return u'%s: /n %s %s  %s %s' % (self.title, self.sub_title, self
                                      .description,self.description_2, self.created_at)

    def __str__(self):
        return f"{self.title} - {self.sub_title}"
