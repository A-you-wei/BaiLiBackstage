import sys

sys.path.append('../')  # 新加入的
from selenium import webdriver
from Configfile.config import *
from selenium.webdriver.common.keys import Keys
import time
import requests
import json
from Configfile.SettingFile import *


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


def fun(page1):
    fromdata = {'page': str(page1), 'rp': '20', 'usepager': 'true', 'table_name': 't_156', 'fields': Field156}
    response = s.post(url, headers=headers, data=fromdata, timeout=50)
    print('当前页数：', json.loads(response.text)['page'], '数据总数:', json.loads(response.text)['total'])
    for data in json.loads(response.text)['rows']:
        id = data['id']
        select1 = "select id from hc_bl_case where id='" + str(id) + "'"
        if sqlFeatures1(select1):
            print('Data already exists')
        else:
            id = data['id']
            name = data['name']
            if name == None:
                name = ''
            else:
                name = str(name).replace("'", "\\'")
            pk_sys_custom_entity_type_1 = data['pk_sys_custom_entity_type_1']
            if pk_sys_custom_entity_type_1 == None:
                pk_sys_custom_entity_type_1 = ''
            else:
                pk_sys_custom_entity_type_1 = str(pk_sys_custom_entity_type_1).replace("'", "\\'")
            casetype_singlebox = data['casetype_singlebox']
            if casetype_singlebox == None:
                casetype_singlebox = ''
            else:
                casetype_singlebox = str(casetype_singlebox).replace("'", "\\'")
            # pk_t_2_1 = data['pk_t_2_1']
            # if pk_t_2_1 == None:
            pk_t_2_1 = ''
            # else:
            #     pk_t_2_1 = str(pk_t_2_1).replace("'", "\\'")
            pk_t_153_2 = data['pk_t_153_2']
            if pk_t_153_2 == None:
                pk_t_153_2 = ''
            else:
                pk_t_153_2 = str(pk_t_153_2).replace("'", "\\'")
            pk_t_217_2 = data['pk_t_217_2']
            if pk_t_217_2 == None:
                pk_t_217_2 = ''
            else:
                pk_t_217_2 = str(pk_t_217_2).replace("'", "\\'")
            pk_t_156_2 = data['pk_t_156_2']
            if pk_t_156_2 == None:
                pk_t_156_2 = ''
            else:
                pk_t_156_2 = str(pk_t_156_2).replace("'", "\\'")
            pk_t_174_3 = data['pk_t_174_3']
            if pk_t_174_3 == None:
                pk_t_174_3 = ''
            else:
                pk_t_174_3 = str(pk_t_174_3).replace("'", "\\'")
            pk_t_174_2 = data['pk_t_174_2']
            if pk_t_174_2 == None:
                pk_t_174_2 = ''
            else:
                pk_t_174_2 = str(pk_t_174_2).replace("'", "\\'")
            pk_t_175_2 = data['pk_t_175_2']
            if pk_t_175_2 == None:
                pk_t_175_2 = ''
            else:
                pk_t_175_2 = str(pk_t_175_2).replace("'", "\\'")
            pk_t_176_2 = data['pk_t_176_2']
            if pk_t_176_2 == None:
                pk_t_176_2 = ''
            else:
                pk_t_176_2 = str(pk_t_176_2).replace("'", "\\'")
            pk_t_178_2 = data['pk_t_178_2']
            if pk_t_178_2 == None:
                pk_t_178_2 = ''
            else:
                pk_t_178_2 = str(pk_t_178_2).replace("'", "\\'")
            pk_t_169_2 = data['pk_t_169_2']
            if pk_t_169_2 == None:
                pk_t_169_2 = ''
            else:
                pk_t_169_2 = str(pk_t_169_2).replace("'", "\\'")
            pk_t_183_2 = data['pk_t_183_2']
            if pk_t_183_2 == None:
                pk_t_183_2 = ''
            else:
                pk_t_183_2 = str(pk_t_183_2).replace("'", "\\'")
            pk_t_181_2 = data['pk_t_181_2']
            if pk_t_181_2 == None:
                pk_t_181_2 = ''
            else:
                pk_t_181_2 = str(pk_t_181_2).replace("'", "\\'")
            pk_t_171_2 = data['pk_t_171_2']
            if pk_t_171_2 == None:
                pk_t_171_2 = ''
            else:
                pk_t_171_2 = str(pk_t_171_2).replace("'", "\\'")
            pk_t_279_2 = data['pk_t_279_2']
            if pk_t_279_2 == None:
                pk_t_279_2 = ''
            else:
                pk_t_279_2 = str(pk_t_279_2).replace("'", "\\'")
            pk_t_203_2 = data['pk_t_203_2']
            if pk_t_203_2 == None:
                pk_t_203_2 = ''
            else:
                pk_t_203_2 = str(pk_t_203_2).replace("'", "\\'")
            toefl_decimal = data['toefl_decimal']
            if toefl_decimal == None:
                toefl_decimal = ''
            else:
                toefl_decimal = str(toefl_decimal).replace("'", "\\'")
            ielts_decimal = data['ielts_decimal']
            if ielts_decimal == None:
                ielts_decimal = ''
            else:
                ielts_decimal = str(ielts_decimal).replace("'", "\\'")
            gpa_decimal = data['gpa_decimal']
            if gpa_decimal == None:
                gpa_decimal = ''
            else:
                gpa_decimal = str(gpa_decimal).replace("'", "\\'")
            gre_varchar = data['gre_varchar']
            if gre_varchar == None:
                gre_varchar = ''
            else:
                gre_varchar = str(gre_varchar).replace("'", "\\'")
            sat_varchar = data['sat_varchar']
            if sat_varchar == None:
                sat_varchar = ''
            else:
                sat_varchar = str(sat_varchar).replace("'", "\\'")
            gmat_varchar = data['gmat_varchar']
            if gmat_varchar == None:
                gmat_varchar = ''
            else:
                gmat_varchar = str(gmat_varchar).replace("'", "\\'")
            ssatscore_decimal = data['ssatscore_decimal']
            if ssatscore_decimal == None:
                ssatscore_decimal = ''
            else:
                ssatscore_decimal = str(ssatscore_decimal).replace("'", "\\'")
            littletoeflscore_decimal = data['littletoeflscore_decimal']
            if littletoeflscore_decimal == None:
                littletoeflscore_decimal = ''
            else:
                littletoeflscore_decimal = str(littletoeflscore_decimal).replace("'", "\\'")
            slepscore_decimal = data['slepscore_decimal']
            if slepscore_decimal == None:
                slepscore_decimal = ''
            else:
                slepscore_decimal = str(slepscore_decimal).replace("'", "\\'")
            gre_decimal = data['gre_decimal']
            if gre_decimal == None:
                gre_decimal = ''
            else:
                gre_decimal = str(gre_decimal).replace("'", "\\'")
            sat_decimal = data['sat_decimal']
            if sat_decimal == None:
                sat_decimal = ''
            else:
                sat_decimal = str(sat_decimal).replace("'", "\\'")
            gmat_decimal = data['gmat_decimal']
            if gmat_decimal == None:
                gmat_decimal = ''
            else:
                gmat_decimal = str(gmat_decimal).replace("'", "\\'")
            actscore_decimal = data['actscore_decimal']
            if actscore_decimal == None:
                actscore_decimal = ''
            else:
                actscore_decimal = str(actscore_decimal).replace("'", "\\'")
            nonescore_decimal = data['nonescore_decimal']
            if nonescore_decimal == None:
                nonescore_decimal = ''
            else:
                nonescore_decimal = str(nonescore_decimal).replace("'", "\\'")
            ntwoscore_decimal = data['ntwoscore_decimal']
            if ntwoscore_decimal == None:
                ntwoscore_decimal = ''
            else:
                ntwoscore_decimal = str(ntwoscore_decimal).replace("'", "\\'")
            gpaTwo_decimal = data['gpaTwo_decimal']
            if gpaTwo_decimal == None:
                gpaTwo_decimal = ''
            else:
                gpaTwo_decimal = str(gpaTwo_decimal).replace("'", "\\'")
            lsat_decimal = data['lsat_decimal']
            if lsat_decimal == None:
                lsat_decimal = ''
            else:
                lsat_decimal = str(lsat_decimal).replace("'", "\\'")

            sql1 = "insert into hc_bl_case(id,name,pk_sys_custom_entity_type_1,casetype_singlebox,pk_t_2_1,pk_t_153_2,pk_t_217_2,pk_t_156_2,pk_t_174_3,pk_t_174_2,pk_t_175_2,pk_t_176_2,pk_t_178_2,pk_t_169_2,pk_t_183_2,pk_t_181_2,pk_t_171_2,pk_t_279_2,pk_t_203_2,toefl_decimal,ielts_decimal,gpa_decimal,gre_varchar,sat_varchar,gmat_varchar,ssatscore_decimal,littletoeflscore_decimal,slepscore_decimal,gre_decimal,sat_decimal,gmat_decimal,actscore_decimal,nonescore_decimal,ntwoscore_decimal,gpaTwo_decimal,lsat_decimal)" \
                   "values('"+str(id)+"','"+str(name)+"','"+str(pk_sys_custom_entity_type_1)+"','"+str(casetype_singlebox)+"','"+str(pk_t_2_1)+"','"+str(pk_t_153_2)+"','"+str(pk_t_217_2)+"','"+str(pk_t_156_2)+"','"+str(pk_t_174_3)+"','"+str(pk_t_174_2)+"','"+str(pk_t_175_2)+"','"+str(pk_t_176_2)+"','"+str(pk_t_178_2)+"','"+str(pk_t_169_2)+"','"+str(pk_t_183_2)+"','"+str(pk_t_181_2)+"','"+str(pk_t_171_2)+"','"+str(pk_t_279_2)+"','"+str(pk_t_203_2)+"','"+str(toefl_decimal)+"','"+str(ielts_decimal)+"','"+str(gpa_decimal)+"','"+str(gre_varchar)+"','"+str(sat_varchar)+"','"+str(gmat_varchar)+"','"+str(ssatscore_decimal)+"','"+str(littletoeflscore_decimal)+"','"+str(slepscore_decimal)+"','"+str(gre_decimal)+"','"+str(sat_decimal)+"','"+str(gmat_decimal)+"','"+str(actscore_decimal)+"','"+str(nonescore_decimal)+"','"+str(ntwoscore_decimal)+"','"+str(gpaTwo_decimal)+"','"+str(lsat_decimal)+"')"
            print(sql1)
            sqlFeatures1(sql1)

if __name__ == '__main__':
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%H', local_time)
    for page1 in range(1, 20):
        print('页数：', page1)
        time_stamp1 = time.time()
        local_time1 = time.localtime(time_stamp1)
        str_time1 = time.strftime('%H', local_time1)
        if page1 == 1:
            s = requests.session()
            cookie = getCookie()
            add_cookies(cookie, s)
        elif str_time != str_time1:
            s = requests.session()
            cookie = getCookie()
            add_cookies(cookie, s)
            str_time = str_time1
        fun(page1)
