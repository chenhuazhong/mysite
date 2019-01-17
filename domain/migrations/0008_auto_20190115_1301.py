# Generated by Django 2.1.3 on 2019-01-15 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0007_auto_20190115_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='pager',
            name='p_content_uuit',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='文章'),
        ),
        migrations.AddField(
            model_name='pager',
            name='p_title_uuid',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='文章标题的uuid'),
        ),
    ]
