from django.contrib import admin

# Register your models here.
from music import models
from music.models import MusicModel


class MusicAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print(change)
        if not change :
            data = form.files.get('music')
            file_name = data.name
            file_path = '/home/python/{}'.format(file_name)
            f = open(file_path, 'wb+')
            for chunk in data.chunks():
                f.write(chunk)

            print(type(data))
            print(1)

            from utils.upload import uploadFile
            f.close()
            print(uploadFile(file_name, file_path))

            import os
            os.remove(file_path)
            music_url = 'http://pninhah8m.bkt.clouddn.com/' + file_name
            MusicModel.objects.create(name=form.data.get('name'),music=music_url,description=form.data.get('description'),user=request.user)


admin.site.register(models.MusicModel, MusicAdmin)