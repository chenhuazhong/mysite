# Generated by Django 2.1.3 on 2019-02-22 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('domain', '0011_domanmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='domanmodel',
            name='type',
            field=models.CharField(choices=[('page', '文章'), ('project', '其他')], default='page', max_length=20, verbose_name='轮播图类型'),
        ),
    ]
