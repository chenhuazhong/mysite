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
            blog_title_obj = i.xpath('h4/a/text()')
            print("-----l-----")
            print(blog_tag_obj[0].text.strip())

            print(blog_title_obj[1].strip())





if __name__ == '__main__':
    getBlogList()