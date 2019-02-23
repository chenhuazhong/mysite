from django.db import models

class BaseModel(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('跟新时间', auto_now=True)
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    class Meta:
        abstract=True
