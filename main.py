import time
from selenium import webdriver
import csv

# 定义要搜索的关键字
keyword = input("请输入要搜索的商品:")

# 搜索商品功能
def get_product(key):
    # 定位到搜索框
    driver.find_element_by_css_selector('#key').send_keys(keyword)
    # 定位到搜索按钮
    driver.find_element_by_css_selector('.button').click()
    # 防止超时，等待加载，设置为10S
    driver.implicitly_wait(10)
    # 最大化浏览器效果



# 解决懒加载
def drop_down():
    for x in range(1,11,2):
        time.sleep(0.5)
        # 控制翻页
        j = x / 10
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)

# 解析商品数据
def parse_product():
    # 拿到商品集合
    lis = driver.find_elements_by_css_selector('.gl-item')

    for li in lis:
      try:
        # 商品名称
        product_name = li.find_element_by_css_selector('div.p-name a em').text
        # 商品价格
        product_price = li.find_element_by_css_selector('div.p-price strong i').text + '元'
        # 商品评价
        product_comment =  li.find_element_by_css_selector('div.p-commit strong a').text
        # 店铺名称
        product_shop_name = li.find_element_by_css_selector('span.J_im_icon a').text

        print(product_shop_name,product_price,product_comment,product_shop_name)

        with open('data_jd.csv',mode='a',encoding='utf-8',newline='') as f:
            csv_write = csv.writer(f)
            csv_write.writerow([product_name,product_price,product_name,product_shop_name])
      except Exception as e:
       print(e)

# 定义获取下一页
def get_next():
    # 翻到下一个
    driver.find_element_by_css_selector('#J_bottomPage > span.p-num > a.pn-next > em').click()
    driver.implicitly_wait(15)

# 实例化一个浏览器对象
driver = webdriver.Chrome()
driver.get('https://www.jd.com')

# 调用函数
get_product(keyword)
for page in range(100):
    drop_down()
    parse_product()
    get_next()
