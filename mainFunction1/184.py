# import sys
# sys.path.append('../')
from selenium import webdriver
from Configfile.config import *
from Configfile.SettingFile import *
from selenium.webdriver.common.keys import Keys
import time
import requests
import json


# 将cookie信息添加进requests组件中
def add_cookies(cookie, s):
    u"往session添加cookies"
    c = requests.cookies.RequestsCookieJar()
    for i in cookie:  # 添加cookie到CookieJar
        # print(i)
        c.set(i["name"], i["value"])
    s.cookies.update(c)  # 更新session里的cookie
    return s


# 获取cookie信息
def getCookie():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(r'user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data1')
    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe", chrome_options=chrome_options)
    driver.get("http://106.37.177.166:18482/baselib/login.jsp")
    element = driver.find_element_by_id("loginNameId")
    element.clear()
    element.send_keys("10081601")
    element = driver.find_element_by_id("passwordId")
    element.clear()
    element.send_keys("BLtx%321")
    element = driver.find_element_by_id("login")
    element.click()
    time.sleep(5)
    url = driver.current_url
    cookie = driver.get_cookies()
    # print(cookie)
    jsonCookies = json.dumps(cookie)  # 转字符串
    driver.close()
    return cookie


def Mainfunction(page1):
    fromdata = {'page': str(page1), 'rp': '20', 'usepager': 'true', 'table_name': 't_184', 'fields': Field184}
    response = s.post(url, headers=headers, data=fromdata, timeout=50)
    print('当前页数：', json.loads(response.text)['page'], '数据总数:', json.loads(response.text)['total'])
    for data in json.loads(response.text)['rows']:
        select1 = "select id from hc_bl_project_branch where id='" + str(data['id']) + "'"
        if sqlFeatures1(select1):
            print('Data already exists')
        else:
            strs2, strs3 = funData(Field184,data)
            sql1 = "insert into hc_bl_project_branch(" + str(strs3) + ")values(" + str(strs2) + ")"
            print(sql1)
            sqlFeatures1(sql1)


if __name__ == '__main__':
    str_time = time.strftime('%H', time.localtime(time.time()))
    for page1 in range(1, 100):
        print('页数：', page1)
        str_time1 = time.strftime('%H', time.localtime(time.time()))
        if page1 == 1:
            s = requests.session()
            cookie = getCookie()
            add_cookies(cookie, s)
        elif str_time != str_time1:
            s = requests.session()
            cookie = getCookie()
            add_cookies(cookie, s)
            str_time = str_time1
        Mainfunction(page1)
