import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
# 加载webdriver对象驱动
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
# 创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox') # 这个很重要
driver = webdriver.Chrome(options=chrome_options) # chromedriver环境加载
email = input('请输入你的德鸡邮箱或ID'+ '\n')
password = input('请输入你的德鸡密码'+ '\n')
# 打开euserv登录界面
driver.get('https://support.euserv.com/')
time.sleep(5)
driver.find_element_by_name('email').send_keys('email')
driver.find_element_by_name('password').send_keys('password')
driver.find_element_by_name('Submit').click()
time.sleep(2)
try:
    x = driver.find_element_by_xpath('//*[@id="kc2_order_customer_orders_tab_content_0"]/div/div[1]/table/tbody/tr[2]/td[1]/img')
    driver.find_element_by_link_text('extend contract').click()
    time.sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="kc2_customer_contract_details_change_plan_item_container_13448"]/tbody/tr/td[2]/input').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="kc2_security_password_dialog_form"]/input[4]').send_keys('kujie2001')
    driver.find_element_by_id('kc2_security_password_dialog_action_confirm').click()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="kc2_customer_contract_details_extend_contract_confirmation_dialog_action_container"]/input[2]').click()
    print('德鸡续费成功!')
except:
        print("无续费小鸡")
