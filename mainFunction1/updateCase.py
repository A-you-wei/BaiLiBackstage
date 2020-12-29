import sys

sys.path.append('../')  # 新加入的
# print(sys.path)
from selenium import webdriver
from Conifg1.config import *
from selenium.webdriver.common.keys import Keys
import time
import requests
import json
import re
from lxml import etree

db_conn = redis.ConnectionPool(host="127.0.0.1", port=6379)
redis_conn_0 = redis.Redis(connection_pool=db_conn, max_connections=10, db=0)


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
    fromdata = {
        'page': str(page1),
        'rp': '100',
        'usepager': 'true',
        'table_name': 't_217',
        'fields': 'id,name,description_textarea,applydegree_singlebox,applyYear_singlebox,applySeason_singlebox,submittime_date,receiveenrolltime_date,istransmajorapply_singlebox,ishavescholarship_singlebox,isentrance_singlebox,isinterview_singlebox,ismagneticset_singlebox,isneedreadlanguage_singlebox,pk_t_153_2,pk_t_154_3,pk_t_155_2,pk_t_159_2,pk_t_169_3,pk_t_174_2,pk_t_175_2,pk_t_176_2,pk_t_183_3,pk_t_184_3,pk_t_181_2,pk_t_174_3,pk_t_172_2,pk_t_173_2,pk_t_178_2,pk_t_284_2,pk_t_180_3,pk_t_203_2,pk_t_283_2,pk_t_279_2,pk_t_171_2,pk_t_2_2,offerimg_img,signingDate_date,serviceState_varchar,schoolrank_decimal,isenrollcon_singlebox,interviewtime_date,submitportfolio_singlebox,schoolnum_varchar,isabandonschool_singlebox,isfullaward_singlebox,admissionResults_singlebox,jiangjin_varchar,rxsj_varchar,grade_decimal,tfdsf_date,sdf_date,zx_varchar,md_varchar,sq_varchar,applybatch_singlebox,researchSubject_varchar,pk_sys_custom_entity_type_1'
    }
    url = "http://106.37.177.166:18482/baselib/CustomManager/queryCustomManager.do?_=1586435487079"
    try:
        response = s.post(url, headers=headers, data=fromdata, timeout=50)
        datalist = json.loads(response.text)['rows']
        page = json.loads(response.text)['page']
        total = json.loads(response.text)['total']
        print('当前页数：', page)
        print('数据总数:', total)
        for data in datalist:
            id = data['id']
            name1 = data['name']
            if name1 == None:
                name = ''
            else:
                name = re.compile('tname=217>(.*?)</span>', re.S).findall(name1)[0].replace("'", "\\'").replace(",", "\\,")
            description_textarea = data['description_textarea']
            if description_textarea == None:
                description_textarea = ''
            else:
                description_textarea = str(description_textarea).replace("'", "\\'")
            applydegree_singlebox = data['applydegree_singlebox']
            if applydegree_singlebox == None:
                applydegree_singlebox = ''
            else:
                applydegree_singlebox = str(applydegree_singlebox).replace("'", "\\'")
            applyYear_singlebox = data['applyYear_singlebox']
            if applyYear_singlebox == None:
                applyYear_singlebox = ''
            else:
                applyYear_singlebox = str(applyYear_singlebox).replace("'", "\\'")
            applySeason_singlebox = data['applySeason_singlebox']
            if applySeason_singlebox == None:
                applySeason_singlebox = ''
            else:
                applySeason_singlebox = str(applySeason_singlebox).replace("'", "\\'")
            submittime_date = data['submittime_date']
            if submittime_date == None:
                submittime_date = ''
            else:
                submittime_date = str(submittime_date).replace("'", "\\'")
            receiveenrolltime_date = data['receiveenrolltime_date']
            if receiveenrolltime_date == None:
                receiveenrolltime_date = ''
            else:
                receiveenrolltime_date = str(receiveenrolltime_date).replace("'", "\\'")
            istransmajorapply_singlebox = data['istransmajorapply_singlebox']
            if istransmajorapply_singlebox == None:
                istransmajorapply_singlebox = ''
            else:
                istransmajorapply_singlebox = str(istransmajorapply_singlebox).replace("'", "\\'")
            ishavescholarship_singlebox = data['ishavescholarship_singlebox']
            if ishavescholarship_singlebox == None:
                ishavescholarship_singlebox = ''
            else:
                ishavescholarship_singlebox = str(ishavescholarship_singlebox).replace("'", "\\'")
            isentrance_singlebox = data['isentrance_singlebox']
            if isentrance_singlebox == None:
                isentrance_singlebox = ''
            else:
                isentrance_singlebox = str(isentrance_singlebox).replace("'", "\\'")
            isinterview_singlebox = data['isinterview_singlebox']
            if isinterview_singlebox == None:
                isinterview_singlebox = ''
            else:
                isinterview_singlebox = str(isinterview_singlebox).replace("'", "\\'")
            ismagneticset_singlebox = data['ismagneticset_singlebox']
            if ismagneticset_singlebox == None:
                ismagneticset_singlebox = ''
            else:
                ismagneticset_singlebox = str(ismagneticset_singlebox).replace("'", "\\'")
            isneedreadlanguage_singlebox = data['isneedreadlanguage_singlebox']
            if isneedreadlanguage_singlebox == None:
                isneedreadlanguage_singlebox = ''
            else:
                isneedreadlanguage_singlebox = str(isneedreadlanguage_singlebox).replace("'", "\\'")
            pk_t_153_2 = data['pk_t_153_2']
            if pk_t_153_2 == None:
                pk_t_153_2 = ''
            else:
                pk_t_153_2 = str(pk_t_153_2).replace("'", "\\'")
            pk_t_154_3 = data['pk_t_154_3']
            if pk_t_154_3 == None:
                pk_t_154_3 = ''
            else:
                pk_t_154_3 = str(pk_t_154_3).replace("'", "\\'")
            pk_t_155_2 = data['pk_t_155_2']
            if pk_t_155_2 == None:
                pk_t_155_2 = ''
            else:
                pk_t_155_2 = str(pk_t_155_2).replace("'", "\\'")
            pk_t_159_2 = data['pk_t_159_2']
            if pk_t_159_2 == None:
                pk_t_159_2 = ''
            else:
                pk_t_159_2 = str(pk_t_159_2).replace("'", "\\'")
            pk_t_169_3 = data['pk_t_169_3']
            if pk_t_169_3 == None:
                pk_t_169_3 = ''
            else:
                pk_t_169_3 = str(pk_t_169_3).replace("'", "\\'")
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
            pk_t_183_3 = data['pk_t_183_3']
            if pk_t_183_3 == None:
                pk_t_183_3 = ''
            else:
                pk_t_183_3 = str(pk_t_183_3).replace("'", "\\'")
            pk_t_184_3 = data['pk_t_184_3']
            if pk_t_184_3 == None:
                pk_t_184_3 = ''
            else:
                pk_t_184_3 = str(pk_t_184_3).replace("'", "\\'")
            pk_t_181_2 = data['pk_t_181_2']
            if pk_t_181_2 == None:
                pk_t_181_2 = ''
            else:
                pk_t_181_2 = str(pk_t_181_2).replace("'", "\\'")
            pk_t_174_3 = data['pk_t_174_3']
            if pk_t_174_3 == None:
                pk_t_174_3 = ''
            else:
                pk_t_174_3 = str(pk_t_174_3).replace("'", "\\'")
            pk_t_172_2 = data['pk_t_172_2']
            if pk_t_172_2 == None:
                pk_t_172_2 = ''
            else:
                pk_t_172_2 = str(pk_t_172_2).replace("'", "\\'")
            pk_t_173_2 = data['pk_t_173_2']
            if pk_t_173_2 == None:
                pk_t_173_2 = ''
            else:
                pk_t_173_2 = str(pk_t_173_2).replace("'", "\\'")
            pk_t_178_2 = data['pk_t_178_2']
            if pk_t_178_2 == None:
                pk_t_178_2 = ''
            else:
                pk_t_178_2 = str(pk_t_178_2).replace("'", "\\'")
            pk_t_284_2 = data['pk_t_284_2']
            if pk_t_284_2 == None:
                pk_t_284_2 = ''
            else:
                pk_t_284_2 = str(pk_t_284_2).replace("'", "\\'")
            pk_t_180_3 = data['pk_t_180_3']
            if pk_t_180_3 == None:
                pk_t_180_3 = ''
            else:
                pk_t_180_3 = str(pk_t_180_3).replace("'", "\\'")
            pk_t_203_2 = data['pk_t_203_2']
            if pk_t_203_2 == None:
                pk_t_203_2 = ''
            else:
                pk_t_203_2 = str(pk_t_203_2).replace("'", "\\'")
            pk_t_283_2 = data['pk_t_283_2']
            if pk_t_283_2 == None:
                pk_t_283_2 = ''
            else:
                pk_t_283_2 = str(pk_t_283_2).replace("'", "\\'")
            pk_t_279_2 = data['pk_t_279_2']
            if pk_t_279_2 == None:
                pk_t_279_2 = ''
            else:
                pk_t_279_2 = str(pk_t_279_2).replace("'", "\\'")
            pk_t_171_2 = data['pk_t_171_2']
            if pk_t_171_2 == None:
                pk_t_171_2 = ''
            else:
                pk_t_171_2 = str(pk_t_171_2).replace("'", "\\'")
            pk_t_2_2 = data['pk_t_2_2']
            if pk_t_2_2 == None:
                pk_t_2_2 = ''
            else:
                pk_t_2_2 = str(pk_t_2_2).replace("'", "\\'")
            offerimg_img = data['offerimg_img']
            if offerimg_img == None:
                offerimg_img = ''
            else:
                offerimg_img = str(offerimg_img).replace("'", "\\'")
            signingDate_date = data['signingDate_date']
            if signingDate_date == None:
                signingDate_date = ''
            else:
                signingDate_date = str(signingDate_date).replace("'", "\\'")
            serviceState_varchar = data['serviceState_varchar']
            if serviceState_varchar == None:
                serviceState_varchar = ''
            else:
                serviceState_varchar = str(serviceState_varchar).replace("'", "\\'")
            schoolrank_decimal = data['schoolrank_decimal']
            if schoolrank_decimal == None:
                schoolrank_decimal = ''
            else:
                schoolrank_decimal = str(schoolrank_decimal).replace("'", "\\'")
            isenrollcon_singlebox = data['isenrollcon_singlebox']
            if isenrollcon_singlebox == None:
                isenrollcon_singlebox = ''
            else:
                isenrollcon_singlebox = str(isenrollcon_singlebox).replace("'", "\\'")
            interviewtime_date = data['interviewtime_date']
            if interviewtime_date == None:
                interviewtime_date = ''
            else:
                interviewtime_date = str(interviewtime_date).replace("'", "\\'")
            submitportfolio_singlebox = data['submitportfolio_singlebox']
            if submitportfolio_singlebox == None:
                submitportfolio_singlebox = ''
            else:
                submitportfolio_singlebox = str(submitportfolio_singlebox).replace("'", "\\'")
            schoolnum_varchar = data['schoolnum_varchar']
            if schoolnum_varchar == None:
                schoolnum_varchar = ''
            else:
                schoolnum_varchar = str(schoolnum_varchar).replace("'", "\\'")
            isabandonschool_singlebox = data['isabandonschool_singlebox']
            if isabandonschool_singlebox == None:
                isabandonschool_singlebox = ''
            else:
                isabandonschool_singlebox = str(isabandonschool_singlebox).replace("'", "\\'")
            isfullaward_singlebox = data['isfullaward_singlebox']
            if isfullaward_singlebox == None:
                isfullaward_singlebox = ''
            else:
                isfullaward_singlebox = str(isfullaward_singlebox).replace("'", "\\'")
            admissionResults_singlebox = data['admissionResults_singlebox']
            if admissionResults_singlebox == None:
                admissionResults_singlebox = ''
            else:
                admissionResults_singlebox = str(admissionResults_singlebox).replace("'", "\\'")
            jiangjin_varchar = data['jiangjin_varchar']
            if jiangjin_varchar == None:
                jiangjin_varchar = ''
            else:
                jiangjin_varchar = str(jiangjin_varchar).replace("'", "\\'")
            rxsj_varchar = data['rxsj_varchar']
            if rxsj_varchar == None:
                rxsj_varchar = ''
            else:
                rxsj_varchar = str(rxsj_varchar).replace("'", "\\'")
            grade_decimal = data['grade_decimal']
            if grade_decimal == None:
                grade_decimal = ''
            else:
                grade_decimal = str(grade_decimal).replace("'", "\\'")
            tfdsf_date = data['tfdsf_date']
            if tfdsf_date == None:
                tfdsf_date = ''
            else:
                tfdsf_date = str(tfdsf_date).replace("'", "\\'")
            sdf_date = data['sdf_date']
            if sdf_date == None:
                sdf_date = ''
            else:
                sdf_date = str(sdf_date).replace("'", "\\'")
            zx_varchar = data['zx_varchar']
            if zx_varchar == None:
                zx_varchar = ''
            else:
                zx_varchar = str(zx_varchar).replace("'", "\\'")
            md_varchar = data['md_varchar']
            if md_varchar == None:
                md_varchar = ''
            else:
                md_varchar = str(md_varchar).replace("'", "\\'")
            sq_varchar = data['sq_varchar']
            if sq_varchar == None:
                sq_varchar = ''
            else:
                sq_varchar = str(sq_varchar).replace("'", "\\'")
            applybatch_singlebox = data['applybatch_singlebox']
            if applybatch_singlebox == None:
                applybatch_singlebox = ''
            else:
                applybatch_singlebox = str(applybatch_singlebox).replace("'", "\\'")
            researchSubject_varchar = data['researchSubject_varchar']
            if researchSubject_varchar == None:
                researchSubject_varchar = ''
            else:
                researchSubject_varchar = str(researchSubject_varchar).replace("'", "\\'")
            pk_sys_custom_entity_type_1 = data['pk_sys_custom_entity_type_1']
            if pk_sys_custom_entity_type_1 == None:
                pk_sys_custom_entity_type_1 = ''
            else:
                pk_sys_custom_entity_type_1 = str(pk_sys_custom_entity_type_1).replace("'", "\\'")
            sqlselect = "select id from hc_bl_apply where id='"+str(id)+"'"
            if sqlFeatures(sqlselect):
                print(sqlFeatures(sqlselect))
                pass
            else:
                sqlInsert = "insert into hc_bl_apply(id,name,description_textarea,applydegree_singlebox,applyYear_singlebox,applySeason_singlebox,submittime_date,receiveenrolltime_date,istransmajorapply_singlebox,ishavescholarship_singlebox,isentrance_singlebox,isinterview_singlebox,ismagneticset_singlebox,isneedreadlanguage_singlebox,pk_t_153_2,pk_t_154_3,pk_t_155_2,pk_t_159_2,pk_t_169_3,pk_t_174_2,pk_t_175_2,pk_t_176_2,pk_t_183_3,pk_t_184_3,pk_t_181_2,pk_t_174_3,pk_t_172_2,pk_t_173_2,pk_t_178_2,pk_t_284_2,pk_t_180_3,pk_t_203_2,pk_t_283_2,pk_t_279_2,pk_t_171_2,pk_t_2_2,offerimg_img,signingDate_date,serviceState_varchar,schoolrank_decimal,isenrollcon_singlebox,interviewtime_date,submitportfolio_singlebox,schoolnum_varchar,isabandonschool_singlebox,isfullaward_singlebox,admissionResults_singlebox,jiangjin_varchar,rxsj_varchar,grade_decimal,tfdsf_date,sdf_date,zx_varchar,md_varchar,sq_varchar,applybatch_singlebox,researchSubject_varchar,pk_sys_custom_entity_type_1)" \
                            "values ('"+str(id)+"','"+str(name)+"','"+str(description_textarea)+"','"+str(applydegree_singlebox)+"','"+str(applyYear_singlebox)+"','"+str(applySeason_singlebox)+"','"+str(submittime_date)+"','"+str(receiveenrolltime_date)+"','"+str(istransmajorapply_singlebox)+"','"+str(ishavescholarship_singlebox)+"','"+str(isentrance_singlebox)+"','"+str(isinterview_singlebox)+"','"+str(ismagneticset_singlebox)+"','"+str(isneedreadlanguage_singlebox)+"','"+str(pk_t_153_2)+"','"+str(pk_t_154_3)+"','"+str(pk_t_155_2)+"','"+str(pk_t_159_2)+"','"+str(pk_t_169_3)+"','"+str(pk_t_174_2)+"','"+str(pk_t_175_2)+"','"+str(pk_t_176_2)+"','"+str(pk_t_183_3)+"','"+str(pk_t_184_3)+"','"+str(pk_t_181_2)+"','"+str(pk_t_174_3)+"','"+str(pk_t_172_2)+"','"+str(pk_t_173_2)+"','"+str(pk_t_178_2)+"','"+str(pk_t_284_2)+"','"+str(pk_t_180_3)+"','"+str(pk_t_203_2)+"','"+str(pk_t_283_2)+"','"+str(pk_t_279_2)+"','"+str(pk_t_171_2)+"','"+str(pk_t_2_2)+"','"+str(offerimg_img)+"','"+str(signingDate_date)+"','"+str(serviceState_varchar)+"','"+str(schoolrank_decimal)+"','"+str(isenrollcon_singlebox)+"','"+str(interviewtime_date)+"','"+str(submitportfolio_singlebox)+"','"+str(schoolnum_varchar)+"','"+str(isabandonschool_singlebox)+"','"+str(isfullaward_singlebox)+"','"+str(admissionResults_singlebox)+"','"+str(jiangjin_varchar)+"','"+str(rxsj_varchar)+"','"+str(grade_decimal)+"','"+str(tfdsf_date)+"','"+str(sdf_date)+"','"+str(zx_varchar)+"','"+str(md_varchar)+"','"+str(sq_varchar)+"','"+str(applybatch_singlebox)+"','"+str(researchSubject_varchar)+"','"+str(pk_sys_custom_entity_type_1)+"')"
                print(sqlInsert)
                sqlFeatures(sqlInsert)
    except Exception as e:
        print(e)
        with open('F:\\DataPy\\mainFunction1\\error2\\217.txt', 'a+', encoding='utf-8') as file:
            file.write(str(page1) + ',')


if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36"}
    time_stamp = time.time()
    local_time = time.localtime(time_stamp)
    str_time = time.strftime('%H', local_time)
    for page1 in range(1,1493):
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
