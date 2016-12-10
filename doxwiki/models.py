import os
from django.db import models
from django.utils.text import slugify
from .marker import Marker
import datetime

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=300) # ADD: lowercase/slug checking
    slug = models.SlugField(max_length=300, unique=True)
    content = models.TextField()
    date_created = models.DateTimeField()
    date_modified = models.DateTimeField()
    tags = models.ManyToManyField('Tag', blank=True)
    categories = models.ManyToManyField('Category', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.date_modified = datetime.datetime.now()
        super().save(*args, **kwargs)

    @property
    def html(self):
        return Marker().to_html(self.content)

    def __str__(self):
        return "{}".format(self.title)


def page_upload_path(instance, filename):
    return os.path.join('attachments', str(instance.page.id), filename) 


class Attachment(models.Model):
    file = models.FileField(upload_to=page_upload_path)
    page = models.ForeignKey(Page)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return "{}".format(self.file.name)


class Tag(models.Model):
    name = models.SlugField(unique=True)

    def __str__(self):
        return "{}".format(self.name)


class Category(models.Model):
    name = models.SlugField(unique=True)
    parent = models.ForeignKey('self', models.SET_NULL, null=True, blank=True, related_name='child_set')

    def __str__(self):
        return "{}".format(self.name)
