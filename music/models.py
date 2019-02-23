import datetime
import os
from time import time
from django.db import models

# Create your models here.
from utils.basemodel import BaseModel


def check_music_url(obj, file_obj):
    """

    :return: 返回图片保存的路径
    """
    # uuid_name = str(uuid.uuid1())[0:5]
    uuid_name = str(time() * 10).split('.')[0]
    new_file_name = uuid_name + '.' + file_obj.split('.')[1]
    # new_file_name = '111.jpg'
    print(new_file_name)
    return os.path.join('{}{}'.format(datetime.datetime.now().strftime("%Y/%m/%d/"),new_file_name))




class MusicModel(BaseModel):
    name = models.CharField(max_length=50, verbose_name='歌曲名')
    music = models.FileField(upload_to=check_music_url, max_length=128, verbose_name='音乐')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name='上传人')
    description = models.CharField(max_length=128, null=True, blank=True, verbose_name='描述')

    class Meta:
        db_table = 'tb_music'
        verbose_name_plural = '音乐'
        verbose_name = '音乐'
