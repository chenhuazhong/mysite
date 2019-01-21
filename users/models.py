import os
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from pip._vendor.distro import os_release_attr

from mysite.settings import BASE_DIR


def user_img():
    return '{}'.format(os.path.join(BASE_DIR, 'templates/../static/images'))


class User(AbstractUser):
    mobile = models.CharField('电话', max_length=11)
    ater_img = models.ImageField('头像', blank=True, null=True, upload_to=user_img)
    csdn_username = models.CharField(max_length=30, verbose_name='csdn账户', help_text='用于模拟登陆csdn', blank=True, null=True)
    csdn_passworld = models.CharField(max_length=30, verbose_name='csdn密码', help_text='用于模拟登陆csdn', blank=True, null=True)

    class Meta:
        db_table='tb_user'
        verbose_name='用户'
        verbose_name_plural = verbose_name

