"""
处理表中的字段
"""
from Configfile.SettingFile import *
from Configfile.config import *
import re

for key in listdict:
    name = key.split('Field')[-1]  # 获取数据表对应得数字
    fields = listdict[key].split(',')  # 每张表得对应得字段
    table = table_name[int(name)]  # 获取得表名字
    for index in fields:
        select156 = "select id as ids,"+str(index)+" from "+str(table)+""
        for i in sqlFeatures1(select156):
            print(i)
            ids = i['ids']
            if index == 'name':
                if 'span' in i[index]:
                    title = re.compile('tname=.*?>(.*?)</span>').findall(i[index],re.S)[0]
                    print(index+':'+ids,title)
            else:
                try:
                    if 'span' in i[index]:
                        print(i[index])
                        dataid = re.compile('dataid=(.*?) ').findall(i[index],re.S)[0]
                        print(index +':',dataid)
                except Exception as e:
                    print(e)

    break

