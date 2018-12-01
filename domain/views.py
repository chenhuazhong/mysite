import json
import re
from collections import OrderedDict

from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render

from domain.models import Pager, Comment
from mysite import settings
from users.utils import login_wrapper


def index(request):
    user = request.user
    user_id = user.id
    if not  user.is_authenticated:
        user = None
        user_id = 'false'

    page  = Pager.objects.filter(p_top=0).order_by('-create_time').all()[:10]
    page_list = []
    for i in page:
        page_dict = OrderedDict()
        page_dict['id'] = i.id
        page_dict['p_title'] = i.p_title
        page_dict['p_commit_number'] = i.p_comment
        print('评论数', i.p_comment)
        page_dict['p_content'] = '<p>' + re.sub('<.*?>', '', i.p_content)[:200] + "</p>"
        print('lailailai')
        print( page_dict['p_content'] )
        page_dict['update_time'] = i.update_time.strftime('%Y-%m-%d')
        # page_dict['id'] = i.id
        page_list.append(page_dict)

    top_page = Pager.objects.filter(p_top=1).all()[: 4]
    top_page_list = []
    for i in top_page:
        top_page_dict = OrderedDict()
        top_page_dict['id'] = i.id
        top_page_dict['p_title'] = i.p_title
        top_page_dict['p_image'] = settings.MEDIA_URL + i.p_img.name
        top_page_dict['p_content'] = '<p>' + re.sub('<. *?>', '', i.p_content)[:200] + "</p>"
        print( top_page_dict['p_content'] )
        top_page_dict['update_time'] = i.update_time
        print("*" * 18)
        print(top_page_dict['p_image'])
        top_page_list.append(top_page_dict)
    top_page_number = top_page.count()
    if top_page_number < 5:
        top_page_ = Pager.objects.order_by('-p_like').all()[: 5 - top_page_number]
        for i in top_page_:
            top_page_dict = OrderedDict()
            top_page_dict['id'] = i.id
            top_page_dict['p_title'] = i.p_title
            top_page_dict['p_image'] = settings.MEDIA_URL + i.p_img.name
            top_page_dict['p_coutent'] = i.p_content
            top_page_dict['update_time'] = i.update_time.strftime('%Y-%m-%d')
            top_page_list.append(top_page_dict)
            print("*"*18)
            print(top_page_dict['p_image'])
    return render(request, template_name='index.html', context= {
        "user": user,
        "user_id": user_id,
        'HOST': settings.HOST,
        'top_page': top_page_list,
        'page': page_list
    })

def detail(request, pk):
    """
    文章详情页
    :param request:
    :return:
    """
    user = request.user
    if user.is_anonymous:
        user=None
    try:
        page = Pager.objects.get(id=pk)
    except Pager.DoesNotExist as e:
        return render(request, '404.html')
    except Exception as e:
        return render(request, '500.html')
    if Comment.objects.filter(page_id=page.id).count():

        comment = Comment.objects.filter(page_id=page.id)
        comm_list = []
        for i in comment:

            comm_dict = OrderedDict()
            comm_dict['id'] = i.id
            comm_dict['username'] = i.user.username
            comm_dict['p_comment'] = i.p_comment
            comm_dict['create_time'] = i.create_time.strftime('%Y-%m-%d')
            if i.comment_set.count():
                comm_list_ = []
                for ii in i.comment_set.all():
                    comm_dict_ = OrderedDict()
                    comm_dict_['id'] = ii.id
                    comm_dict_['username'] = ii.user.username
                    comm_dict_['p_comment'] = ii.p_comment
                    comm_dict_['create_time'] = ii.create_time.strftime('%Y-%m-%d')
                    comm_list_.append(comm_dict_)
                comm_dict['comm'] = comm_list_

            comm_list.append(comm_dict)

    else:
        comm_list =None


    return render(request, 'page.html', context={
        'HOST': settings.HOST,
        'user': user,
        'page': page,
        'comment': comm_list
    })



@login_wrapper
def comment(request, pk):
    print(request.user)
    page = Pager.objects.get(id=pk)

    comment = Comment()
    comment.page_id=page.id
    comment.p_comment=json.loads(request.body.decode('utf-8')).get('comment')
    comment.user = request.user
    comment.save()

    page.p_comment += 1
    page.save()

    return JsonResponse({'code':200, 'message': '评论已提交'})