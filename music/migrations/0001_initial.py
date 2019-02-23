# Generated by Django 2.1.3 on 2019-02-23 08:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import music.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicMoel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='跟新时间')),
                ('name', models.CharField(max_length=50, verbose_name='歌曲名')),
                ('music', models.FileField(max_length=128, upload_to=music.models.check_music_url, verbose_name='音乐')),
                ('description', models.CharField(blank=True, max_length=128, null=True, verbose_name='描述')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='上传人')),
            ],
            options={
                'verbose_name': '音乐',
                'db_table': 'tb_music',
                'verbose_name_plural': '音乐',
            },
        ),
    ]
