from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Pager)
admin.site.register(models.Comment)