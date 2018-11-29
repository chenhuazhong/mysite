import os
import uuid
from time import time

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
import datetime

from mysite.settings import BASE_DIR
from users.models import User
from utils.basemodel import BaseModel

def check_img_url(obj, file_obj):
    """

    :return: 返回图片保存的路径
    """
    # uuid_name = str(uuid.uuid1())[0:5]
    uuid_name = str(time() * 10).split('.')[0]
    new_file_name = uuid_name + '.' + file_obj.split('.')[1]
    # new_file_name = '111.jpg'
    print(new_file_name)
    return os.path.join('{}{}'.format(datetime.datetime.now().strftime("%Y/%m/%d/"),new_file_name))


class Pager(BaseModel):

    CHOICES_TOP = (
        (0, '不置顶'),
        (1, '置顶'),
    )
    p_user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='文章发布者', default=User.objects.get(username='root').id)
    p_like = models.IntegerField('点赞数', default=0)
    p_comment = models.IntegerField('评论数', default=0)
    p_content = RichTextUploadingField('文章内容')
    p_title = models.CharField('文章标题', max_length=128)
    p_img = models.ImageField('首页图片', upload_to=check_img_url, blank=True, null=True, max_length=100)
    p_isdelete = models.BooleanField('逻辑删除', default=False)
    p_top = models.SmallIntegerField('首页轮播图（置顶）', choices=CHOICES_TOP, default=0)

    class Meta:
        db_table='tb_pager'
        verbose_name='文章'
        verbose_name_plural=verbose_name


class Comment(BaseModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    page = models.ForeignKey('Pager', on_delete=models.CASCADE)
    p_comment = models.CharField('评论', max_length=500)
    c_comment = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table='tb_comment'
        verbose_name='评论表'
        verbose_name_plural='评论表'



