import hashlib

from django.contrib import admin

# Register your models here.
from utils.csdn_selenium import publish_csdn_page
from . import models


class PagerAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print('mark--page')
        print(form.data['p_type'])
        print(int(form.data['p_type']) == 1)
        print('---',(int(form.data['p_type']) == 1) and (obj is None))
        if int(form.data['p_type']) == 1:
            if not change:
                print(11)
                # publish_csdn_page(form.data['p_title'], form.data['p_content'])
                md = hashlib.md5(form.data['p_title'].encode('utf-8'))
                title_md5 = md.hexdigest()
                md2 = hashlib.md5(form.data['p_content'].encode('utf-8'))
                content_md5 = md2.hexdigest()
                # form.data['p_title_md5'] = title_md5
                # form.data['p_content'] = content_md5
            print(type(change))

        # if obj is None :
        else:
            super().save_model(request, obj, form, change)


admin.site.register(models.Pager, PagerAdmin)
admin.site.register(models.Comment)