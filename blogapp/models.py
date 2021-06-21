from django.conf import settings
from django.utils.timezone import now
from django.utils import timezone

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    objects = EntryQuerySet.as_manager()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Blog Entry"
        verbose_name_plural = "Blog Entries"
        ordering = ["-created"]


class comment(models.Model):
    ID= models.AutoField(primary_key=True,verbose_name='ID')
    hello = models.ForeignKey(Entry,related_name="comments", on_delete=models.CASCADE,default=None)
    name= models.CharField(max_length=50, null=True)
    comment = models.TextField()
    creates = models.DateTimeField(auto_now_add=timezone.now())

    def __str__(self):
        return 'comment by {} on {}'.format(self.name, self.hello)

    class Meta:
        ordering = ["-creates"]
