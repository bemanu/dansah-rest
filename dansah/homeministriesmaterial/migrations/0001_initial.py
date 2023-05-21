# Generated by Django 4.2.1 on 2023-05-20 14:41

import homeministriesmaterial.uploadfiles
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeMinistriesMaterial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Intro tile')),
                ('sub_title', models.CharField(max_length=255, verbose_name='Sub-title')),
                ('text', models.CharField(max_length=1024, verbose_name='Intro text')),
                ('icon_image', models.ImageField(blank=True, null=True, upload_to=homeministriesmaterial.uploadfiles.upload_image_path, verbose_name='Icon image')),
                ('icon_image_path', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(verbose_name='update at')),
            ],
        ),
        migrations.CreateModel(
            name='MinistriesMaterial',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Ministries material title')),
                ('description', models.CharField(max_length=1024, verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=homeministriesmaterial.uploadfiles.upload_image_path, verbose_name='Icon image')),
                ('image_path', models.CharField(max_length=255)),
                ('redirect_link', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(verbose_name='update at')),
            ],
        ),
    ]