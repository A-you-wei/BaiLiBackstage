from lxml import etree
from lxml.html import tostring
import pymysql
import re
import math
import json


# 连接mysql数据库
def sqlFeatures(sql_statement=None):
    conn = pymysql.connect(host='39.106.71.70', user='lixu', password='lixu1006', db='hidaas', port=3306)
    cursor = conn.cursor()
    # conn = pymysql.connect(host='47.104.25.221', user='xuhang', password='xuhang', db='xuhang', port=3306)
    # cursor = conn.cursor()
    # conn = pymysql.connect(host='47.104.25.221', user='xuhang', password='xuhang', db='ms', port=3306)
    # cursor = conn.cursor()
    # 志娟本地数据库
    # conn = pymysql.connect(host='192.168.20.32', user='root', password='root', db='test', port=3306)
    # cursor = conn.cursor()
    """
    :查询的增删改查
    :param sql_statement:
    :return:
    """
    if 'insert' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'select' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()
    elif 'update' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'show' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()


# 连接mysql数据库
def sqlFeatures1(sql_statement=None):
    # conn = pymysql.connect(host='39.106.71.70', user='lixu', password='lixu1006', db='hidaas', port=3306)
    # cursor = conn.cursor()
    # conn = pymysql.connect(host='47.104.25.221', user='xuhang', password='xuhang', db='xuhang', port=3306)
    # cursor = conn.cursor()
    conn = pymysql.connect(host='47.104.25.221', user='xuhang', password='xuhang', db='ms', port=3306)
    cursor = conn.cursor()
    # 志娟本地数据库
    # conn = pymysql.connect(host='192.168.20.32', user='root', password='root', db='hidaas', port=3306)
    # cursor = conn.cursor()
    """
    :查询的增删改查
    :param sql_statement:
    :return:
    """
    if 'insert' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        stepId = conn.insert_id()
        conn.commit()
        return stepId
    elif 'select' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()
    elif 'update' in sql_statement:
        sql = sql_statement
        cursor.execute(sql)
        conn.commit()
    elif 'show' in sql_statement:
        sql = sql_statement
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        cur.execute(sql)
        return cur.fetchall()


# 封装得xpath方法
def xpaths(response1=None, div=None):
    """
    :返回xpath解析的对象
    :param response1:
    :param div:
    :return:
    """
    divlist = etree.HTML(response1).xpath(div)
    return divlist


# 封装tostring方法（返回得为html）
def tostrings(htmllist, code):
    """
    :解析xpath返回的对像list
    ：循环返回解析后的html文本
    :return:
    """
    for html in htmllist:
        html1 = tostring(html, encoding=code).decode(code)
        yield html1


# 暂时无用
def fun1(strdata, data, table):
    """
    :拼接字符串得到返回值
    ：返回值为list
    :param strdata:
    :param data:
    :return:
    """
    strings = strdata.split(',')
    listStr = []
    for index in strings:
        if index == 'name':
            name = data[index]
            if name == None:
                name = ''
            else:
                name = re.compile('tname=' + str(table) + '>(.*?)</span>', re.S).findall(name)[0].replace("'",
                                                                                                          "\\'")
            listStr.append(name)
        else:
            if data[index] == None:
                index = ''
            else:
                index = str(data[index]).replace("'", "\\'")
            listStr.append(index)
    return listStr


# 暂时无用
def SplicingSql(fdata, dataList, table, table_name):
    """
    :拼接sql语句
    :param fdata:
    :param dataList:
    :param table_name:
    :return:
    """
    sqlIsert = "insert into `" + str(table_name) + "`(" + str(fdata) + ")values(" + str(dataList) + ")"
    return sqlIsert


# 拼接sql语句字段以及把值为None得修改成 ''
def funData(datastr,fdata):
    """
    拼接sql语句字段以及把值为None得修改成 ''
    :param data:
    :return:
    """
    strs2 = ''
    strs3 = ''
    for key in datastr.split(','):
        if fdata[key] == None:
            fdata[key] = ''
        else:
            fdata[key] = str(fdata[key]).replace("'", "\\'")
        strs2 += "'" + str(fdata[key]) + "',"
        strs3 += '' + str(key) + ','
    return strs2[:-1], strs3[:-1]


# 获取页数
def total(table_name, s):
    """
    获取页数得函数（百利后台系统）
    :param table_name:
    :param s:
    :return:
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36",
    }
    fromdata = {
        'page': 1,
        'rp': '100',
        'usepager': 'true',
        'table_name': 't_' + str(table_name),
        'fields': 'id'
    }
    url = "http://106.37.177.166:18482/baselib/CustomManager/queryCustomManager.do?_=1586435487079"
    response = s.post(url, headers=headers, data=fromdata, timeout=25)
    print(response.text)
    total = json.loads(response.text)['total']
    page = math.ceil(total / 100) + 1
    return page


# 获取数据库所有得表
def showTables():
    """
    获取数据库所有得表
    :return:
    """
    sqlSelect = "show tables"
    data = sqlFeatures(sqlSelect)
    tableList = []
    for tables in data:
        table = tables['Tables_in_hidaas']
        tableList.append(table)
    return tableList


# 获取数据表中得所有得字段
def sqlField(table_name=None):
    sqlname = "select COLUMN_NAME from information_schema.COLUMNS where table_name = '" + str(table_name) + "'"
    strlist = []
    for index in sqlFeatures(sqlname):
        strlist.append(index['COLUMN_NAME'])
    strs = ','.join(strlist)
    return strs
