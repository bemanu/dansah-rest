# Generated by Django 4.2.1 on 2023-05-23 18:51

import homeslider.uploadfiles
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Home slider title')),
                ('image', models.ImageField(blank=True, null=True, upload_to=homeslider.uploadfiles.upload_image_path, verbose_name='Image')),
                ('image1', models.ImageField(blank=True, null=True, upload_to=homeslider.uploadfiles.upload_image_path, verbose_name='Image 1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to=homeslider.uploadfiles.upload_image_path, verbose_name='Image 2')),
                ('image_path', models.CharField(max_length=255, verbose_name='Image')),
                ('image_path_1', models.CharField(max_length=255, verbose_name='Image 1')),
                ('image_path_2', models.CharField(max_length=255, verbose_name='Image 2')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateField(verbose_name='update at')),
            ],
            options={
                'ordering': ('title', 'created_at'),
            },
        ),
        migrations.CreateModel(
            name='Intro',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Intro tile')),
                ('sub_title', models.CharField(max_length=255, verbose_name='Sub tile')),
                ('text', models.CharField(max_length=1024, verbose_name='Intro text')),
                ('image_path', models.ImageField(blank=True, null=True, upload_to=homeslider.uploadfiles.upload_image_path, verbose_name='Image')),
                ('icon_image_path', models.ImageField(blank=True, null=True, upload_to=homeslider.uploadfiles.upload_image_path, verbose_name='Icon')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'ordering': ('title', 'sub_title', 'text', 'created_at'),
            },
        ),
    ]
