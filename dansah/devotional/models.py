import os
import uuid
from datetime import date
from random import random

from django.db import models


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "devotion/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Devotional(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    devotion_title = models.CharField("Devotion title", max_length=255)
    devotion_message = models.CharField("Devotion message", max_length=2048)
    devotion_date = models.DateField("Devotion date",default=date.today())
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    devotion_created_at = models.DateTimeField(auto_now_add=True)
    devotion_updated_at = models.DateTimeField(auto_now_add=True)
    devotion_monthly = models.BooleanField("Monthly devotion", default=False)

    class Meta:
        ordering = ("devotion_title", "devotion_date")


    def __unicode__(self):
        return u'%s: /n %s' % (self.devotion_title,
                               self.devotion_message)
