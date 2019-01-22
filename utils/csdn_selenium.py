from selenium import webdriver
import time

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
        driver.find_element_by_link_text('开始创作').click()
    except Exception as e:
        print('没有获取到开始') #todo
        pass
    driver.find_element_by_id('txtTitle').send_keys('haha')
    driver.switch_to_frame(driver.find_element_by_xpath("//iframe[@class='cke_wysiwyg_frame cke_reset']"))
    driver.find_element_by_xpath('//body/p').send_keys('haha')
    time.sleep(3)

if __name__ == '__main__':
    spider_login_csdn()


