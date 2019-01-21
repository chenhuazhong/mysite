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
            blog_tag_obj = i.xpath('h4/a/span')[0]
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
            print(blog_tag_obj.text.strip())
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
                        'p_other_id': blog_data_id,
                        'p_tag': blog_tag_obj,
                        'p_type': 1
                    })

            else:
                pagetr = Pager.objects.create(**{
                    'p_title': blog_title_obj,
                    'p_content': page_detil_html_code,
                    'p_title_md5': title_md5,
                    'p_content_md5': content_md5,
                    'p_other_id': blog_data_id,
                    'p_tag': blog_tag_obj,
                    'p_type': 1
                })


def GetJinShuPage():
    header = {'user-agent':"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
    result = requests.get('https://www.jianshu.com/u/659497dff7e1',
    headers=header)
    html_obj = etree.HTML(result.content.decode('utf-8'))
    page_list = html_obj.xpath('//ul[@class="note-list"]/li')
    for page in page_list:
        blog_data_id = page.xpath('@data-note-id')[0]
        page_detil_url_ = page.xpath('div/a/@href')[0]
        page_detil_url = 'https://www.jianshu.com/{}'.format(page_detil_url_)
        result_detil = requests.get(page_detil_url, headers = header)
        # print(result_.content.decode('utf-8'))
        html_detil_obj = etree.HTML(result_detil.content.decode('utf-8'))
        page_detil_obj = html_detil_obj.xpath('//div[@class="article"]')[0]
        page_title = page_detil_obj.xpath('h1/text()')[0]
        page_content_html_obj = page_detil_obj.xpath("div[@class='show-content']")[0]
        page_content_html_str = etree.tostring(page_content_html_obj,encoding='utf-8').decode('utf-8')
        print(page_content_html_str)
        import os
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings_dev')
        import django
        django.setup()
        #
        md = hashlib.md5(page_title.encode('utf-8'))
        title_md5 = md.hexdigest()
        md2 = hashlib.md5(page_content_html_str.encode('utf-8'))
        content_md5 = md2.hexdigest()
        from domain.models import Pager

        if Pager.objects.filter(p_other_id=blog_data_id).exists():

            if not Pager.objects.filter(p_other_id=blog_data_id, p_title_md5=title_md5,
                                        p_content_md5=content_md5).exists():
                pagetr = Pager.objects.filter(p_other_id=blog_data_id).update(**{
                    'p_title': page_title,
                    'p_content': page_content_html_str,
                    'p_title_md5': title_md5,
                    'p_content_md5': content_md5,
                    'p_other_id': blog_data_id,
                    'p_type': 2
                })

        else:
            pagetr = Pager.objects.create(**{
                'p_title': page_title,
                'p_content': page_content_html_str,
                'p_title_md5': title_md5,
                'p_content_md5': content_md5,
                'p_other_id': blog_data_id,
                'p_type': 2
            })





            # print(html_obj.xpath("//ul[@class='note-list']/li").text)

def main():
    GetJinShuPage()
    getBlogList()


if __name__ == '__main__':
    main()
