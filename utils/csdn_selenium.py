from selenium import webdriver
import time

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


def spider_login_csdn():

    import os
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    import django
    django.setup()
    from users.models import User

    url = "https://passport.csdn.net/login"
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    driver.get(url)
    driver.find_element_by_xpath('//div[@class="main-select"]//li[1]/a').click()
    # 输入账号
    csdn_username = User.objects.get(username='root').csdn_username
    csdn_passworld = User.objects.get(username='root').csdn_passworld
    driver.find_element_by_id('all').send_keys(csdn_username)
    # 输入密码
    driver.find_element_by_id('password-number').send_keys(csdn_passworld)
    time.sleep(1)
    print(driver.window_handles)
    print(driver.find_element_by_tag_name("button").text)
    driver.find_element_by_tag_name("button").click()
    time.sleep(3)
    driver.quit()
    # driver.switch_to_frame()

def publish_csdn_page(title, content):
    # import os
    # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    # import django
    # django.setup()
    from users.models import User
    from pyvirtualdisplay import Display
    url = "https://passport.csdn.net/login"
    # 开始没有显示界面的chrome 浏览器
    chrome_options = Options()
    chrome_options.add_argument('--headless')

    # 低于59版本的chrome浏览器  需要开启一个虚拟界面 来跑chrome 无界面模式
    # 高于59 版本的chrome浏览器 不需要开启虚拟界面来跑 chrome浏览器的无头模式
    display = Display(visible=False, size=(1024, 768))  # 需要安装 sudo apt-get install xvfb
    display.start()
    # chrome浏览器的驱动根据 本地装的chrome浏览器的版本下载 相关驱动
    # 将驱动复制到 /usr/local/bin/chromedriver
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
    driver.get(url)
    driver.find_element_by_xpath('//div[@class="main-select"]//li[1]/a').click()
    # 输入账号
    csdn_username = User.objects.get(username='root').csdn_username
    csdn_passworld = User.objects.get(username='root').csdn_passworld
    driver.find_element_by_id('all').send_keys(csdn_username)
    # 输入密码
    driver.find_element_by_id('password-number').send_keys(csdn_passworld)
    time.sleep(1)
    print(driver.window_handles)
    print(driver.find_element_by_tag_name("button").text)
    driver.find_element_by_tag_name("button").click()
    print(driver.window_handles)
    time.sleep(8)

    # print(driver.find_element_by_tag_name("button").click())
    try:
        driver.find_element_by_xpath("//div[@class='indexSuperise']/button").click()
    except Exception as e:
        pass
    driver.find_element_by_xpath("//ul[@class='btns']/li[3]/a/span").click()
    time.sleep(3)
    try:
        print(driver.window_handles)
        driver.switch_to_window(driver.window_handles[1])
        driver.switch_to_alert()
        driver.find_element_by_id('btnStart').click()
        driver.switch_to_default_content()
    except Exception as e:
        print('没有获取到开始', e)  # todo
        pass
    driver.find_element_by_id('txtTitle').send_keys(title)
    driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']"))
    # driver.find_element_by_xpath('//body/p').click()
    driver.find_element_by_xpath('//body').send_keys(content)
    time.sleep(1)
    driver.switch_to_default_content()
    select1 = Select(driver.find_element_by_id('selType'))
    select1.select_by_visible_text('原创')
    select2 = Select(driver.find_element_by_id('radChl'))
    select2.select_by_visible_text('后端')
    time.sleep(1)
    driver.find_element_by_id('btnPublish').click()

    driver.quit()
    # driver.switch_to_frame()
if __name__ == '__main__':
    publish_csdn_page('mysite publish','mysite publish')


