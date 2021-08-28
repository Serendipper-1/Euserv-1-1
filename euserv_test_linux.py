


# 创建一个参数对象，用来控制chrome以无界面模式打开
import sys
import time

from requests import post
from selenium import webdriver

TG_TOKEN = ''   # 通过 @BotFather 申请获得
CHAT_ID = ''      # 用户、群组或频道 ID
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox') # 这个很重要
driver = webdriver.Chrome(options=chrome_options) # chromedriver环境加载


def post_tg(message):
    telegram_message = f"{message}"

    params = (
        ('chat_id', CHAT_ID),
        ('text', telegram_message),
        ('parse_mode', "Markdown"),  # 可选Html或Markdown
        ('disable_web_page_preview', "yes")
    )
    telegram_url = "https://api.telegram.org/bot" + TG_TOKEN + "/sendMessage"
    telegram_req = post(telegram_url, params=params)
    telegram_status = telegram_req.status_code
    if telegram_status == 200:
        print(f"TG消息已推送")
    else:
        print("Telegram Error")
def iselement():
    """
    基本实现判断元素是否存在
    :param browser: 浏览器对象
    :param xpaths: xpaths表达式
    :return: 是否存在
    """
    try:
        driver.find_element_by_xpath('//*[@id="kc2_order_customer_orders_tab_0"]')
        return True
    except:
        return False


def login(email, password):
    # 打开euserv登录界面
    driver.get('https://support.euserv.com/')
    time.sleep(5)

    driver.find_element_by_name('email').send_keys(email)
    driver.find_element_by_name('password').send_keys(password)
    driver.find_element_by_name('Submit').click()
    d = iselement()
    if d == False:
        print("登录失败,请检查用户名及密码!!或账户被删请检查!!")
        post_tg('登录失败,账户似乎被删除惹')
        sys.exit(1)
    time.sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="kc2_order_customer_orders_tab_content_1"]/table/tbody/tr[2]/td[4]/div/span/form/input[1]')
        post_tg('恭喜你'+ email + '小鸡成功开出!!!')

    except:
        post_tg(email+ '小鸡还未通过')
        print('小鸡还未通过')


if __name__ == '__main__':
    j = 0
    n = 1
    login1 = [
        'admin@admin.com','123456',   # 在此处填写用户名或密码 示例
        'XXXX','XXXX',
    ]
    le = int(len(login1)/2)
    for i in range(le):
        login(login1[j], login1[n])
        j = j+2
        n = n+2
