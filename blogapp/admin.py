from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Entry)
admin.site.register(models.comment)