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


def fun(page1):
    fromdata = {'page': str(page1), 'rp': '20', 'usepager': 'true', 'table_name': 't_237', 'fields': Field237}
    response = s.post(url, headers=headers, data=fromdata, timeout=50)
    print('当前页数：', json.loads(response.text)['page'], '数据总数:', json.loads(response.text)['total'])
    for data in json.loads(response.text)['rows']:
        id = data['id']
        select1 = "select id from hc_bl_background where id='" + str(id) + "'"
        if sqlFeatures1(select1):
            print('Data already exists')
        else:
            id = data['id']
            pk_t_161_2 = data['pk_t_161_2']
            if pk_t_161_2 == None:
                pk_t_161_2 = ''
            else:
                pk_t_161_2 = str(pk_t_161_2).replace("'", "\\'")
            pk_t_174_2 = data['pk_t_174_2']
            if pk_t_174_2 == None:
                pk_t_174_2 = ''
            else:
                pk_t_174_2 = str(pk_t_174_2).replace("'", "\\'")
            pk_t_178_2 = data['pk_t_178_2']
            if pk_t_178_2 == None:
                pk_t_178_2 = ''
            else:
                pk_t_178_2 = str(pk_t_178_2).replace("'", "\\'")
            hasAcadPro_singlebox = data['hasAcadPro_singlebox']
            if hasAcadPro_singlebox == None:
                hasAcadPro_singlebox = ''
            else:
                hasAcadPro_singlebox = str(hasAcadPro_singlebox).replace("'", "\\'")
            partTime_textarea = data['partTime_textarea']
            if partTime_textarea == None:
                partTime_textarea = ''
            else:
                partTime_textarea = str(partTime_textarea).replace("'", "\\'")
            labName_textarea = data['labName_textarea']
            if labName_textarea == None:
                labName_textarea = ''
            else:
                labName_textarea = str(labName_textarea).replace("'", "\\'")
            labLevel_textarea = data['labLevel_textarea']
            if labLevel_textarea == None:
                labLevel_textarea = ''
            else:
                labLevel_textarea = str(labLevel_textarea).replace("'", "\\'")
            duration_varchar = data['duration_varchar']
            if duration_varchar == None:
                duration_varchar = ''
            else:
                duration_varchar = str(duration_varchar).replace("'", "\\'")
            level_singlebox = data['level_singlebox']
            if level_singlebox == None:
                level_singlebox = ''
            else:
                level_singlebox = str(level_singlebox).replace("'", "\\'")
            proTitle_varchar = data['proTitle_varchar']
            if proTitle_varchar == None:
                proTitle_varchar = ''
            else:
                proTitle_varchar = str(proTitle_varchar).replace("'", "\\'")
            proRes_textblock = data['proRes_textblock']
            if proRes_textblock == None:
                proRes_textblock = ''
            else:
                proRes_textblock = str(proRes_textblock).replace("'", "\\'")
            isPublish_singlebox = data['isPublish_singlebox']
            if isPublish_singlebox == None:
                isPublish_singlebox = ''
            else:
                isPublish_singlebox = str(isPublish_singlebox).replace("'", "\\'")
            invMethod_textblock = data['invMethod_textblock']
            if invMethod_textblock == None:
                invMethod_textblock = ''
            else:
                invMethod_textblock = str(invMethod_textblock).replace("'", "\\'")
            hasPaper_singlebox = data['hasPaper_singlebox']
            if hasPaper_singlebox == None:
                hasPaper_singlebox = ''
            else:
                hasPaper_singlebox = str(hasPaper_singlebox).replace("'", "\\'")
            journalName_textarea = data['journalName_textarea']
            if journalName_textarea == None:
                journalName_textarea = ''
            else:
                journalName_textarea = str(journalName_textarea).replace("'", "\\'")
            journalName_singlebox = data['journalName_singlebox']
            if journalName_singlebox == None:
                journalName_singlebox = ''
            else:
                journalName_singlebox = str(journalName_singlebox).replace("'", "\\'")
            severalAuthors_varchar = data['severalAuthors_varchar']
            if severalAuthors_varchar == None:
                severalAuthors_varchar = ''
            else:
                severalAuthors_varchar = str(severalAuthors_varchar).replace("'", "\\'")
            affectoi_textblock = data['affectoi_textblock']
            if affectoi_textblock == None:
                affectoi_textblock = ''
            else:
                affectoi_textblock = str(affectoi_textblock).replace("'", "\\'")
            isPatent_singlebox = data['isPatent_singlebox']
            if isPatent_singlebox == None:
                isPatent_singlebox = ''
            else:
                isPatent_singlebox = str(isPatent_singlebox).replace("'", "\\'")
            hasAcaComp_singlebox = data['hasAcaComp_singlebox']
            if hasAcaComp_singlebox == None:
                hasAcaComp_singlebox = ''
            else:
                hasAcaComp_singlebox = str(hasAcaComp_singlebox).replace("'", "\\'")
            parForm_textarea = data['parForm_textarea']
            if parForm_textarea == None:
                parForm_textarea = ''
            else:
                parForm_textarea = str(parForm_textarea).replace("'", "\\'")
            mainResp_textblock = data['mainResp_textblock']
            if mainResp_textblock == None:
                mainResp_textblock = ''
            else:
                mainResp_textblock = str(mainResp_textblock).replace("'", "\\'")
            isFianls_singlebox = data['isFianls_singlebox']
            if isFianls_singlebox == None:
                isFianls_singlebox = ''
            else:
                isFianls_singlebox = str(isFianls_singlebox).replace("'", "\\'")
            isGetPos_singlebox = data['isGetPos_singlebox']
            if isGetPos_singlebox == None:
                isGetPos_singlebox = ''
            else:
                isGetPos_singlebox = str(isGetPos_singlebox).replace("'", "\\'")
            awards_textblock = data['awards_textblock']
            if awards_textblock == None:
                awards_textblock = ''
            else:
                awards_textblock = str(awards_textblock).replace("'", "\\'")
            awardLevel_textarea = data['awardLevel_textarea']
            if awardLevel_textarea == None:
                awardLevel_textarea = ''
            else:
                awardLevel_textarea = str(awardLevel_textarea).replace("'", "\\'")
            partYear_varchar = data['partYear_varchar']
            if partYear_varchar == None:
                partYear_varchar = ''
            else:
                partYear_varchar = str(partYear_varchar).replace("'", "\\'")
            ramark_textblock = data['ramark_textblock']
            if ramark_textblock == None:
                ramark_textblock = ''
            else:
                ramark_textblock = str(ramark_textblock).replace("'", "\\'")
            mainRespons_textblock = data['mainRespons_textblock']
            if mainRespons_textblock == None:
                mainRespons_textblock = ''
            else:
                mainRespons_textblock = str(mainRespons_textblock).replace("'", "\\'")
            skills_textblock = data['skills_textblock']
            if skills_textblock == None:
                skills_textblock = ''
            else:
                skills_textblock = str(skills_textblock).replace("'", "\\'")
            isTopFiveHundred_singlebox = data['isTopFiveHundred_singlebox']
            if isTopFiveHundred_singlebox == None:
                isTopFiveHundred_singlebox = ''
            else:
                isTopFiveHundred_singlebox = str(isTopFiveHundred_singlebox).replace("'", "\\'")
            compInfluence_textblock = data['compInfluence_textblock']
            if compInfluence_textblock == None:
                compInfluence_textblock = ''
            else:
                compInfluence_textblock = str(compInfluence_textblock).replace("'", "\\'")
            compNum_varchar = data['compNum_varchar']
            if compNum_varchar == None:
                compNum_varchar = ''
            else:
                compNum_varchar = str(compNum_varchar).replace("'", "\\'")
            compTurnover_varchar = data['compTurnover_varchar']
            if compTurnover_varchar == None:
                compTurnover_varchar = ''
            else:
                compTurnover_varchar = str(compTurnover_varchar).replace("'", "\\'")
            positionLevel_varchar = data['positionLevel_varchar']
            if positionLevel_varchar == None:
                positionLevel_varchar = ''
            else:
                positionLevel_varchar = str(positionLevel_varchar).replace("'", "\\'")
            workingTime_varchar = data['workingTime_varchar']
            if workingTime_varchar == None:
                workingTime_varchar = ''
            else:
                workingTime_varchar = str(workingTime_varchar).replace("'", "\\'")
            workContent_textblock = data['workContent_textblock']
            if workContent_textblock == None:
                workContent_textblock = ''
            else:
                workContent_textblock = str(workContent_textblock).replace("'", "\\'")
            workContEval_textblock = data['workContEval_textblock']
            if workContEval_textblock == None:
                workContEval_textblock = ''
            else:
                workContEval_textblock = str(workContEval_textblock).replace("'", "\\'")
            workDepart_varchar = data['workDepart_varchar']
            if workDepart_varchar == None:
                workDepart_varchar = ''
            else:
                workDepart_varchar = str(workDepart_varchar).replace("'", "\\'")
            job_textblock = data['job_textblock']
            if job_textblock == None:
                job_textblock = ''
            else:
                job_textblock = str(job_textblock).replace("'", "\\'")
            workCity_varchar = data['workCity_varchar']
            if workCity_varchar == None:
                workCity_varchar = ''
            else:
                workCity_varchar = str(workCity_varchar).replace("'", "\\'")
            jobSiteAsse_varchar = data['jobSiteAsse_varchar']
            if jobSiteAsse_varchar == None:
                jobSiteAsse_varchar = ''
            else:
                jobSiteAsse_varchar = str(jobSiteAsse_varchar).replace("'", "\\'")
            jobResp_textblock = data['jobResp_textblock']
            if jobResp_textblock == None:
                jobResp_textblock = ''
            else:
                jobResp_textblock = str(jobResp_textblock).replace("'", "\\'")
            from_singlebox = data['from_singlebox']
            if from_singlebox == None:
                from_singlebox = ''
            else:
                from_singlebox = str(from_singlebox).replace("'", "\\'")
            activityContent_textblock = data['activityContent_textblock']
            if activityContent_textblock == None:
                activityContent_textblock = ''
            else:
                activityContent_textblock = str(activityContent_textblock).replace("'", "\\'")
            activityOrg_textarea = data['activityOrg_textarea']
            if activityOrg_textarea == None:
                activityOrg_textarea = ''
            else:
                activityOrg_textarea = str(activityOrg_textarea).replace("'", "\\'")
            activityNum_varchar = data['activityNum_varchar']
            if activityNum_varchar == None:
                activityNum_varchar = ''
            else:
                activityNum_varchar = str(activityNum_varchar).replace("'", "\\'")
            isLeader_singlebox = data['isLeader_singlebox']
            if isLeader_singlebox == None:
                isLeader_singlebox = ''
            else:
                isLeader_singlebox = str(isLeader_singlebox).replace("'", "\\'")
            awardName_textarea = data['awardName_textarea']
            if awardName_textarea == None:
                awardName_textarea = ''
            else:
                awardName_textarea = str(awardName_textarea).replace("'", "\\'")
            eventOrg_textarea = data['eventOrg_textarea']
            if eventOrg_textarea == None:
                eventOrg_textarea = ''
            else:
                eventOrg_textarea = str(eventOrg_textarea).replace("'", "\\'")
            rewardProp_textarea = data['rewardProp_textarea']
            if rewardProp_textarea == None:
                rewardProp_textarea = ''
            else:
                rewardProp_textarea = str(rewardProp_textarea).replace("'", "\\'")
            rewardYear_varchar = data['rewardYear_varchar']
            if rewardYear_varchar == None:
                rewardYear_varchar = ''
            else:
                rewardYear_varchar = str(rewardYear_varchar).replace("'", "\\'")
            cOne_textarea = data['cOne_textarea']
            if cOne_textarea == None:
                cOne_textarea = ''
            else:
                cOne_textarea = str(cOne_textarea).replace("'", "\\'")
            patentDur_varchar = data['patentDur_varchar']
            if patentDur_varchar == None:
                patentDur_varchar = ''
            else:
                patentDur_varchar = str(patentDur_varchar).replace("'", "\\'")
            kaishishiqi_varchar = data['kaishishiqi_varchar']
            if kaishishiqi_varchar == None:
                kaishishiqi_varchar = ''
            else:
                kaishishiqi_varchar = str(kaishishiqi_varchar).replace("'", "\\'")
            qiyeleixing_textarea = data['qiyeleixing_textarea']
            if qiyeleixing_textarea == None:
                qiyeleixing_textarea = ''
            else:
                qiyeleixing_textarea = str(qiyeleixing_textarea).replace("'", "\\'")
            jianglidengji_textarea = data['jianglidengji_textarea']
            if jianglidengji_textarea == None:
                jianglidengji_textarea = ''
            else:
                jianglidengji_textarea = str(jianglidengji_textarea).replace("'", "\\'")
            wenyi_varchar = data['wenyi_varchar']
            if wenyi_varchar == None:
                wenyi_varchar = ''
            else:
                wenyi_varchar = str(wenyi_varchar).replace("'", "\\'")
            sfcjwytt_singlebox = data['sfcjwytt_singlebox']
            if sfcjwytt_singlebox == None:
                sfcjwytt_singlebox = ''
            else:
                sfcjwytt_singlebox = str(sfcjwytt_singlebox).replace("'", "\\'")
            wyttmc_textarea = data['wyttmc_textarea']
            if wyttmc_textarea == None:
                wyttmc_textarea = ''
            else:
                wyttmc_textarea = str(wyttmc_textarea).replace("'", "\\'")
            wyttjb_singlebox = data['wyttjb_singlebox']
            if wyttjb_singlebox == None:
                wyttjb_singlebox = ''
            else:
                wyttjb_singlebox = str(wyttjb_singlebox).replace("'", "\\'")
            tiyu_varchar = data['tiyu_varchar']
            if tiyu_varchar == None:
                tiyu_varchar = ''
            else:
                tiyu_varchar = str(tiyu_varchar).replace("'", "\\'")
            sfcjtytt_singlebox = data['sfcjtytt_singlebox']
            if sfcjtytt_singlebox == None:
                sfcjtytt_singlebox = ''
            else:
                sfcjtytt_singlebox = str(sfcjtytt_singlebox).replace("'", "\\'")
            tyttmc_textarea = data['tyttmc_textarea']
            if tyttmc_textarea == None:
                tyttmc_textarea = ''
            else:
                tyttmc_textarea = str(tyttmc_textarea).replace("'", "\\'")
            tyttjb_singlebox = data['tyttjb_singlebox']
            if tyttjb_singlebox == None:
                tyttjb_singlebox = ''
            else:
                tyttjb_singlebox = str(tyttjb_singlebox).replace("'", "\\'")
            qita_textarea = data['qita_textarea']
            if qita_textarea == None:
                qita_textarea = ''
            else:
                qita_textarea = str(qita_textarea).replace("'", "\\'")
            cylb_singlebox = data['cylb_singlebox']
            if cylb_singlebox == None:
                cylb_singlebox = ''
            else:
                cylb_singlebox = str(cylb_singlebox).replace("'", "\\'")
            cymc_textarea = data['cymc_textarea']
            if cymc_textarea == None:
                cymc_textarea = ''
            else:
                cymc_textarea = str(cymc_textarea).replace("'", "\\'")
            sfkj_singlebox = data['sfkj_singlebox']
            if sfkj_singlebox == None:
                sfkj_singlebox = ''
            else:
                sfkj_singlebox = str(sfkj_singlebox).replace("'", "\\'")
            sfcjgbs_singlebox = data['sfcjgbs_singlebox']
            if sfcjgbs_singlebox == None:
                sfcjgbs_singlebox = ''
            else:
                sfcjgbs_singlebox = str(sfcjgbs_singlebox).replace("'", "\\'")
            bsjb_singlebox = data['bsjb_singlebox']
            if bsjb_singlebox == None:
                bsjb_singlebox = ''
            else:
                bsjb_singlebox = str(bsjb_singlebox).replace("'", "\\'")
            sfhj_singlebox = data['sfhj_singlebox']
            if sfhj_singlebox == None:
                sfhj_singlebox = ''
            else:
                sfhj_singlebox = str(sfhj_singlebox).replace("'", "\\'")
            jbjb_singlebox = data['jbjb_singlebox']
            if jbjb_singlebox == None:
                jbjb_singlebox = ''
            else:
                jbjb_singlebox = str(jbjb_singlebox).replace("'", "\\'")
            mqjb_textarea = data['mqjb_textarea']
            if mqjb_textarea == None:
                mqjb_textarea = ''
            else:
                mqjb_textarea = str(mqjb_textarea).replace("'", "\\'")
            activityCha_textarea = data['activityCha_textarea']
            if activityCha_textarea == None:
                activityCha_textarea = ''
            else:
                activityCha_textarea = str(activityCha_textarea).replace("'", "\\'")
            kaishirq_date = data['kaishirq_date']
            if kaishirq_date == None:
                kaishirq_date = ''
            else:
                kaishirq_date = str(kaishirq_date).replace("'", "\\'")
            jiesuriq_date = data['jiesuriq_date']
            if jiesuriq_date == None:
                jiesuriq_date = ''
            else:
                jiesuriq_date = str(jiesuriq_date).replace("'", "\\'")
            chixushijian_varchar = data['chixushijian_varchar']
            if chixushijian_varchar == None:
                chixushijian_varchar = ''
            else:
                chixushijian_varchar = str(chixushijian_varchar).replace("'", "\\'")
            shifoucanjiabisai_singlebox = data['shifoucanjiabisai_singlebox']
            if shifoucanjiabisai_singlebox == None:
                shifoucanjiabisai_singlebox = ''
            else:
                shifoucanjiabisai_singlebox = str(shifoucanjiabisai_singlebox).replace("'", "\\'")
            bshjqk_textarea = data['bshjqk_textarea']
            if bshjqk_textarea == None:
                bshjqk_textarea = ''
            else:
                bshjqk_textarea = str(bshjqk_textarea).replace("'", "\\'")
            sfhdzyrz_singlebox = data['sfhdzyrz_singlebox']
            if sfhdzyrz_singlebox == None:
                sfhdzyrz_singlebox = ''
            else:
                sfhdzyrz_singlebox = str(sfhdzyrz_singlebox).replace("'", "\\'")
            rzsm_textarea = data['rzsm_textarea']
            if rzsm_textarea == None:
                rzsm_textarea = ''
            else:
                rzsm_textarea = str(rzsm_textarea).replace("'", "\\'")
            sfsfd_textarea = data['sfsfd_textarea']
            if sfsfd_textarea == None:
                sfsfd_textarea = ''
            else:
                sfsfd_textarea = str(sfsfd_textarea).replace("'", "\\'")
            activityStartDate_date = data['activityStartDate_date']
            if activityStartDate_date == None:
                activityStartDate_date = ''
            else:
                activityStartDate_date = str(activityStartDate_date).replace("'", "\\'")
            proLink_web = data['proLink_web']
            if proLink_web == None:
                proLink_web = ''
            else:
                proLink_web = str(proLink_web).replace("'", "\\'")
            name = data['name']
            if name == None:
                name = ''
            else:
                name = str(name).replace("'", "\\'")
            description_textarea = data['description_textarea']
            if description_textarea == None:
                description_textarea = ''
            else:
                description_textarea = str(description_textarea).replace("'", "\\'")
            actualcost_decimal = data['actualcost_decimal']
            if actualcost_decimal == None:
                actualcost_decimal = ''
            else:
                actualcost_decimal = str(actualcost_decimal).replace("'", "\\'")
            approvedamount_decimal = data['approvedamount_decimal']
            if approvedamount_decimal == None:
                approvedamount_decimal = ''
            else:
                approvedamount_decimal = str(approvedamount_decimal).replace("'", "\\'")
            pk_sys_custom_entity_type_1 = data['pk_sys_custom_entity_type_1']
            if pk_sys_custom_entity_type_1 == None:
                pk_sys_custom_entity_type_1 = ''
            else:
                pk_sys_custom_entity_type_1 = str(pk_sys_custom_entity_type_1).replace("'", "\\'")
            pk_sys_custom_approval_period_1 = data['pk_sys_custom_approval_period_1']
            if pk_sys_custom_approval_period_1 == None:
                pk_sys_custom_approval_period_1 = ''
            else:
                pk_sys_custom_approval_period_1 = str(pk_sys_custom_approval_period_1).replace("'", "\\'")
            submit_datetime = data['submit_datetime']
            if submit_datetime == None:
                submit_datetime = ''
            else:
                submit_datetime = str(submit_datetime).replace("'", "\\'")
            approval_datetime = data['approval_datetime']
            if approval_datetime == None:
                approval_datetime = ''
            else:
                approval_datetime = str(approval_datetime).replace("'", "\\'")
            pk_t_53_1 = data['pk_t_53_1']
            if pk_t_53_1 == None:
                pk_t_53_1 = ''
            else:
                pk_t_53_1 = str(pk_t_53_1).replace("'", "\\'")
            pk_t_2_1 = data['pk_t_2_1']
            if pk_t_2_1 == None:
                pk_t_2_1 = ''
            else:
                pk_t_2_1 = str(pk_t_2_1).replace("'", "\\'")
            close_datetime = data['close_datetime']
            if close_datetime == None:
                close_datetime = ''
            else:
                close_datetime = str(close_datetime).replace("'", "\\'")
            pk_t_235_2 = data['pk_t_235_2']
            if pk_t_235_2 == None:
                pk_t_235_2 = ''
            else:
                pk_t_235_2 = str(pk_t_235_2).replace("'", "\\'")
            practicetype_singlebox = data['practicetype_singlebox']
            if practicetype_singlebox == None:
                practicetype_singlebox = ''
            else:
                practicetype_singlebox = str(practicetype_singlebox).replace("'", "\\'")
            paperType_singlebox = data['paperType_singlebox']
            if paperType_singlebox == None:
                paperType_singlebox = ''
            else:
                paperType_singlebox = str(paperType_singlebox).replace("'", "\\'")
            paperRole_textarea = data['paperRole_textarea']
            if paperRole_textarea == None:
                paperRole_textarea = ''
            else:
                paperRole_textarea = str(paperRole_textarea).replace("'", "\\'")
            patentName_varchar = data['patentName_varchar']
            if patentName_varchar == None:
                patentName_varchar = ''
            else:
                patentName_varchar = str(patentName_varchar).replace("'", "\\'")
            patentType_textarea = data['patentType_textarea']
            if patentType_textarea == None:
                patentType_textarea = ''
            else:
                patentType_textarea = str(patentType_textarea).replace("'", "\\'")
            workPosi_varchar = data['workPosi_varchar']
            if workPosi_varchar == None:
                workPosi_varchar = ''
            else:
                workPosi_varchar = str(workPosi_varchar).replace("'", "\\'")
            partRole_singlebox = data['partRole_singlebox']
            if partRole_singlebox == None:
                partRole_singlebox = ''
            else:
                partRole_singlebox = str(partRole_singlebox).replace("'", "\\'")
            pk_t_153_2 = data['pk_t_153_2']
            if pk_t_153_2 == None:
                pk_t_153_2 = ''
            else:
                pk_t_153_2 = str(pk_t_153_2).replace("'", "\\'")
            xqlx_singlebox = data['xqlx_singlebox']
            if xqlx_singlebox == None:
                xqlx_singlebox = ''
            else:
                xqlx_singlebox = str(xqlx_singlebox).replace("'", "\\'")
            timeAxis_date = data['timeAxis_date']
            if timeAxis_date == None:
                timeAxis_date = ''
            else:
                timeAxis_date = str(timeAxis_date).replace("'", "\\'")
            describe_blob = data['describe_blob']
            if describe_blob == None:
                describe_blob = ''
            else:
                describe_blob = str(describe_blob).replace("'", "\\'")

            sql1 = "insert into hc_bl_background(id,pk_t_161_2,pk_t_174_2,pk_t_178_2,hasAcadPro_singlebox,partTime_textarea,labName_textarea,labLevel_textarea,duration_varchar,level_singlebox,proTitle_varchar,proRes_textblock,isPublish_singlebox,invMethod_textblock,hasPaper_singlebox,journalName_textarea,journalName_singlebox,severalAuthors_varchar,affectoi_textblock,isPatent_singlebox,hasAcaComp_singlebox,parForm_textarea,mainResp_textblock,isFianls_singlebox,isGetPos_singlebox,awards_textblock,awardLevel_textarea,partYear_varchar,ramark_textblock,mainRespons_textblock,skills_textblock,isTopFiveHundred_singlebox,compInfluence_textblock,compNum_varchar,compTurnover_varchar,positionLevel_varchar,workingTime_varchar,workContent_textblock,workContEval_textblock,workDepart_varchar,job_textblock,workCity_varchar,jobSiteAsse_varchar,jobResp_textblock,from_singlebox,activityContent_textblock,activityOrg_textarea,activityNum_varchar,isLeader_singlebox,awardName_textarea,eventOrg_textarea,rewardProp_textarea,rewardYear_varchar,cOne_textarea,patentDur_varchar,kaishishiqi_varchar,qiyeleixing_textarea,jianglidengji_textarea,wenyi_varchar,sfcjwytt_singlebox,wyttmc_textarea,wyttjb_singlebox,tiyu_varchar,sfcjtytt_singlebox,tyttmc_textarea,tyttjb_singlebox,qita_textarea,cylb_singlebox,cymc_textarea,sfkj_singlebox,sfcjgbs_singlebox,bsjb_singlebox,sfhj_singlebox,jbjb_singlebox,mqjb_textarea,activityCha_textarea,kaishirq_date,jiesuriq_date,chixushijian_varchar,shifoucanjiabisai_singlebox,bshjqk_textarea,sfhdzyrz_singlebox,rzsm_textarea,sfsfd_textarea,activityStartDate_date,proLink_web,name,description_textarea,actualcost_decimal,approvedamount_decimal,pk_sys_custom_entity_type_1,pk_sys_custom_approval_period_1,submit_datetime,approval_datetime,pk_t_53_1,pk_t_2_1,close_datetime,pk_t_235_2,practicetype_singlebox,paperType_singlebox,paperRole_textarea,patentName_varchar,patentType_textarea,workPosi_varchar,partRole_singlebox,pk_t_153_2,xqlx_singlebox,timeAxis_date,describe_blob)" \
                   "values('"+str(id)+"','"+str(pk_t_161_2)+"','"+str(pk_t_174_2)+"','"+str(pk_t_178_2)+"','"+str(hasAcadPro_singlebox)+"','"+str(partTime_textarea)+"','"+str(labName_textarea)+"','"+str(labLevel_textarea)+"','"+str(duration_varchar)+"','"+str(level_singlebox)+"','"+str(proTitle_varchar)+"','"+str(proRes_textblock)+"','"+str(isPublish_singlebox)+"','"+str(invMethod_textblock)+"','"+str(hasPaper_singlebox)+"','"+str(journalName_textarea)+"','"+str(journalName_singlebox)+"','"+str(severalAuthors_varchar)+"','"+str(affectoi_textblock)+"','"+str(isPatent_singlebox)+"','"+str(hasAcaComp_singlebox)+"','"+str(parForm_textarea)+"','"+str(mainResp_textblock)+"','"+str(isFianls_singlebox)+"','"+str(isGetPos_singlebox)+"','"+str(awards_textblock)+"','"+str(awardLevel_textarea)+"','"+str(partYear_varchar)+"','"+str(ramark_textblock)+"','"+str(mainRespons_textblock)+"','"+str(skills_textblock)+"','"+str(isTopFiveHundred_singlebox)+"','"+str(compInfluence_textblock)+"','"+str(compNum_varchar)+"','"+str(compTurnover_varchar)+"','"+str(positionLevel_varchar)+"','"+str(workingTime_varchar)+"','"+str(workContent_textblock)+"','"+str(workContEval_textblock)+"','"+str(workDepart_varchar)+"','"+str(job_textblock)+"','"+str(workCity_varchar)+"','"+str(jobSiteAsse_varchar)+"','"+str(jobResp_textblock)+"','"+str(from_singlebox)+"','"+str(activityContent_textblock)+"','"+str(activityOrg_textarea)+"','"+str(activityNum_varchar)+"','"+str(isLeader_singlebox)+"','"+str(awardName_textarea)+"','"+str(eventOrg_textarea)+"','"+str(rewardProp_textarea)+"','"+str(rewardYear_varchar)+"','"+str(cOne_textarea)+"','"+str(patentDur_varchar)+"','"+str(kaishishiqi_varchar)+"','"+str(qiyeleixing_textarea)+"','"+str(jianglidengji_textarea)+"','"+str(wenyi_varchar)+"','"+str(sfcjwytt_singlebox)+"','"+str(wyttmc_textarea)+"','"+str(wyttjb_singlebox)+"','"+str(tiyu_varchar)+"','"+str(sfcjtytt_singlebox)+"','"+str(tyttmc_textarea)+"','"+str(tyttjb_singlebox)+"','"+str(qita_textarea)+"','"+str(cylb_singlebox)+"','"+str(cymc_textarea)+"','"+str(sfkj_singlebox)+"','"+str(sfcjgbs_singlebox)+"','"+str(bsjb_singlebox)+"','"+str(sfhj_singlebox)+"','"+str(jbjb_singlebox)+"','"+str(mqjb_textarea)+"','"+str(activityCha_textarea)+"','"+str(kaishirq_date)+"','"+str(jiesuriq_date)+"','"+str(chixushijian_varchar)+"','"+str(shifoucanjiabisai_singlebox)+"','"+str(bshjqk_textarea)+"','"+str(sfhdzyrz_singlebox)+"','"+str(rzsm_textarea)+"','"+str(sfsfd_textarea)+"','"+str(activityStartDate_date)+"','"+str(proLink_web)+"','"+str(name)+"','"+str(description_textarea)+"','"+str(actualcost_decimal)+"','"+str(approvedamount_decimal)+"','"+str(pk_sys_custom_entity_type_1)+"','"+str(pk_sys_custom_approval_period_1)+"','"+str(submit_datetime)+"','"+str(approval_datetime)+"','"+str(pk_t_53_1)+"','"+str(pk_t_2_1)+"','"+str(close_datetime)+"','"+str(pk_t_235_2)+"','"+str(practicetype_singlebox)+"','"+str(paperType_singlebox)+"','"+str(paperRole_textarea)+"','"+str(patentName_varchar)+"','"+str(patentType_textarea)+"','"+str(workPosi_varchar)+"','"+str(partRole_singlebox)+"','"+str(pk_t_153_2)+"','"+str(xqlx_singlebox)+"','"+str(timeAxis_date)+"','"+str(describe_blob)+"')"
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
