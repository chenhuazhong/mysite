# Generated by Django 2.1.3 on 2019-01-15 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0008_auto_20190115_1301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pager',
            old_name='p_content_uuit',
            new_name='p_content_md5',
        ),
        migrations.RenameField(
            model_name='pager',
            old_name='p_title_uuid',
            new_name='p_title_md5',
        ),
    ]
