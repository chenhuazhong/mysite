import hashlib
from uuid import uuid4

import lxml
lxml.get_include()
import requests
from lxml import etree

# Create your tests here.


def getBlogList():

        con = requests.get('https://blog.csdn.net/p571912102')
        # print(len(con.content.decode('utf-8')))
        content = con.content.decode('utf-8')
        html_obj = etree.HTML(content)
        html_str = etree.tostring(html_obj, pretty_print=True)
        blog_obj_list = html_obj.xpath('//div[@data-articleid]')[1:]
        for i in blog_obj_list:
            blog_tag_obj = i.xpath('h4/a/span')
            blog_data_id = int(i.xpath('@data-articleid')[0])
            print('id--->',blog_data_id)
            blog_content_obj = i.xpath('p/a')[0].text
            blog_title_obj = i.xpath('h4/a/text()')[1].strip()
            blog_time_obj_list = i.xpath('//div[@data-articleid][2]/div/p/span') # 发布时间 阅读 评论
            for i in blog_time_obj_list:
                print('---time--',i.text)
            detil_url = 'https://blog.csdn.net/p571912102/article/details/{}'.format(blog_data_id)
            '''获取文章详情'''
            result = requests.get(detil_url)
            detil_html = result.content.decode('utf-8')
            detil_html_obj = etree.HTML(detil_html)
            detil_html_str = etree.tostring(detil_html_obj, pretty_print=True)
            detil_obj = detil_html_obj.xpath('//div[@id="article_content"]')[0]
            page_detil_html_code = etree.tostring(detil_obj, encoding='utf-8').decode('utf-8').replace('\n','<br/>')

            print('detil--->',page_detil_html_code)
            print("-----l-----")
            print(blog_tag_obj[0].text.strip())
            # print('----content-----')
            # print(blog_content_obj)

            print(blog_title_obj)
            import os
            os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings_dev')
            import django
            django.setup()
            #
            md = hashlib.md5(blog_title_obj.encode('utf-8'))
            title_md5 = md.hexdigest()
            md2 = hashlib.md5(page_detil_html_code.encode('utf-8'))
            content_md5 = md2.hexdigest()
            from domain.models import Pager
            if Pager.objects.filter(p_other_id=blog_data_id).exists():

                if not Pager.objects.filter(p_other_id=blog_data_id, p_title_md5 = title_md5, p_content_md5=content_md5).exists():
                    pagetr = Pager.objects.filter(p_other_id=blog_data_id).update(**{
                        'p_title': blog_title_obj,
                        'p_content': page_detil_html_code,
                        'p_title_md5': title_md5,
                        'p_content_md5': content_md5,
                        'p_other_id': blog_data_id
                    })

            else:
                pagetr = Pager.objects.create(**{
                    'p_title': blog_title_obj,
                    'p_content': blog_content_obj,
                    'p_title_md5': title_md5,
                    'p_content_md5': content_md5,
                    'p_other_id': blog_data_id
                })


if __name__ == '__main__':
    getBlogList()
