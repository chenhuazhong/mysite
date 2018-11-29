import re
from collections import OrderedDict

from django.shortcuts import render

# Create your views here.
from domain.models import Pager


def page(request):
    user = request.user
    page_obj_list = Pager.objects.all()[:20]
    pagelist = []
    for obj in page_obj_list:
        page_obj_dict = OrderedDict()
        page_obj_dict['id'] = obj.id
        page_obj_dict['update_time'] = obj.update_time.strftime('%Y-%m-%d')
        page_obj_dict['p_content'] = '<p>' + re.sub('<.*?>', '', obj.p_content)[:400] + "</p>"
        print(page_obj_dict['p_content'])
        page_obj_dict['p_title'] = obj.p_title
        pagelist.append(page_obj_dict)

    return render(request, 'pagelist.html', context={
        'page': pagelist
    })
    pass