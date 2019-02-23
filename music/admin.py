from django.contrib import admin

# Register your models here.
from music import models


class MusicAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.MusicModel, MusicAdmin)