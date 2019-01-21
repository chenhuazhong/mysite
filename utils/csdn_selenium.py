from selenium import webdriver
import time
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
driver.find_element_by_tag_name("button").click()


