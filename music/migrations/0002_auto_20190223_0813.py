# Generated by Django 2.1.3 on 2019-02-23 08:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MusicMoel',
            new_name='MusicModel',
        ),
    ]
