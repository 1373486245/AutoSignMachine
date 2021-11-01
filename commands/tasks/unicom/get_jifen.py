# -*- coding: utf-8 -*-
# @Time    : 2021/08/14 16:30
# @Author  : srcrs
# @Email   : srcrs@foxmail.com
import requests,json,time,re,login,logging,traceback,os,random,notify,datetime
from lxml.html import fromstring

#签到页面任务
class get_jifen:
    def run(self, client, user):
        taskId = ('b5f69c69010d440aaf5c802953a0b325','21b24f8f38a74880a6f9073698af900a','980e1dadca304977819db2b761281868')
        #开始浏览积分商城
        try:
            i=0
            while True:               
                if i==3:
                    break
                elif i<=2:
                    print(taskId[i])
                    data = '{\"taskId\":\"'+taskId[i]+'\",\"systemCode\":\"QDQD\",\"orderId\":\"\"}'
                    client.headers.update({'Host': 'act.10010.com','content-length': '78','pragma': 'no-cache','cache-control': 'no-cache','accept': 'application/json, text/plain, */*','user-agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36; unicom{version:android@8.0804,desmobile:16604372008};devicetype{deviceBrand:Xiaomi,deviceModel:MI 8};{yw_code:}','content-type': 'application/json','origin': 'https://img.client.10010.com','x-requested-with': 'com.sinovatech.unicom.ui','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://img.client.10010.com/SigininApp/index.html','accept-encoding': 'gzip, deflate','accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'})
                    get_jifen = client.post('https://act.10010.com/SigninApp/simplyDotask/accomplishDotask',data=data)
                    get_jifen.encoding='utf-8'
                    res = get_jifen.json()
                    print(res)
                    if res['status'] == '0000':
                        print('【开始积分任务】')
                    else:
                        print('【开始积分任务失败】')
                    time.sleep(1)

                    #浏览结果
                    try:
                        data1 = 'floorMark=superEasy'
                        client.headers.update({'Host': 'act.10010.com','content-length': '19','pragma': 'no-cache','cache-control': 'no-cache','accept': 'application/json, text/plain, */*','user-agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36; unicom{version:android@8.0804,desmobile:16604372008};devicetype{deviceBrand:Xiaomi,deviceModel:MI 8};{yw_code:}','content-type': 'application/x-www-form-urlencoded','origin': 'https://img.client.10010.com','x-requested-with': 'com.sinovatech.unicom.ui','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://img.client.10010.com/SigininApp/index.html','accept-encoding': 'gzip, deflate','accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'})
                        get_jifen1 = client.post('https://act.10010.com/SigninApp/superSimpleTask/getTask',data=data1)
                        get_jifen1.encoding='utf-8'
                        res1 = get_jifen1.json()
                        #print(res1)
                        if res1['data'][0]['achieve'] == '1':
                            logging.info(f'【{res1["data"][0]["title"]}】')
                        else:
                            logging.info(f'【失败】：{res1["msg"]}')
                        time.sleep(1)
                    except Exception as e:
                        print(traceback.format_exc())
                        logging.error('【获取任务状态】: 错误，原因为: ' + str(e))
                    time.sleep(10)
                    #领取积分
                    try:
                        data2 = 'taskId='+taskId[i]
                        client.headers.update({'Host': 'act.10010.com','content-length': '39','pragma': 'no-cache','cache-control': 'no-cache','accept': 'application/json, text/plain, */*','user-agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36; unicom{version:android@8.0804,desmobile:16604372008};devicetype{deviceBrand:Xiaomi,deviceModel:MI 8};{yw_code:}','content-type': 'application/x-www-form-urlencoded','origin': 'https://img.client.10010.com','x-requested-with': 'com.sinovatech.unicom.ui','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://img.client.10010.com/SigininApp/index.html','accept-encoding': 'gzip, deflate','accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'})
                        get_jifen2 = client.post('https://act.10010.com/SigninApp/simplyDotask/doTaskS',data=data2)
                        get_jifen2.encoding='utf-8'
                        res2 = get_jifen2.json()
                        print(res2)
                        if res2['status'] == '0000':
                            logging.info(f'【领取奖励积分】：{res2["data"]["prizeCount"]}积分')
                        else:
                            logging.info(f'【领取奖励积分失败】：{res2["msg"]}')
                        time.sleep(1)
                    except Exception as e:
                        print(traceback.format_exc())
                        logging.error('【领取奖励积分】: 错误，原因为: ' + str(e))
                    i = i+1
                    time.sleep(10)
                    continue
        except Exception as e:
            print(traceback.format_exc())
            logging.error('【积分任务运行失败】: 错误，原因为: ' + str(e))
        time.sleep(20)        
                  
                        
        #大奖励任务
        try:
            data3 = 'floorMark=bigRew'
            client.headers.update({'Host': 'act.10010.com','content-length': '16','pragma': 'no-cache','cache-control': 'no-cache','accept': 'application/json, text/plain, */*','user-agent': 'Mozilla/5.0 (Linux; Android 10; MI 8 Build/QKQ1.190828.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36; unicom{version:android@8.0804,desmobile:16604372008};devicetype{deviceBrand:Xiaomi,deviceModel:MI 8};{yw_code:}','content-type': 'application/x-www-form-urlencoded','origin': 'https://img.client.10010.com','x-requested-with': 'com.sinovatech.unicom.ui','sec-fetch-site': 'same-site','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://img.client.10010.com/SigininApp/index.html','accept-encoding': 'gzip, deflate','accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'})
            get_jifen3 = client.post('https://act.10010.com/SigninApp/superSimpleTask/getTask',data=data3)
            get_jifen3.encoding='utf-8'
            res3 = get_jifen3.json()
            i =0
            while True:
                if i==3:
                    break
                elif i <=2 :  
                    if res3['status'] == '0000':
                        logging.info(f'【任务：{res3["data"][i]["title"]}】已完成{res3["data"][i]["achieve"]}天')
                    else:
                        logging.info(f'【大奖励任务查询失败】：{res3["msg"]}')
                    time.sleep(1)  
                    taskId = (res3['data'][0]['taskId'],res3['data'][1]['taskId'],res3['data'][2]['taskId'],)                
                    #print(res3)
                    if res3['data'][i]['achieve'] == res3['data'][i]['allocation'] and res3['data'][i]['showStyle']== '2':
                        data4 = f'taskId={taskId[i]}'
                        try:
                            get_jifen4 = client.post('https://act.10010.com/SigninApp/simplyDotask/doTaskS',data=data4)
                            get_jifen4.encoding='utf-8'
                            res4 = get_jifen4.json()
                            print(res4)
                            logging.info(f'【领取奖励积分】：{res4["data"]["prizeCount"]}积分')
                        except Exception as e:
                            print(traceback.format_exc())
                            logging.error('【大奖励任务领取】: 错误，原因为: ' + str(e)) 
                        time.sleep(5)                        
                    else:
                        time.sleep(1)
                    i = i+1
                    continue
            time.sleep(1)
        except Exception as e:
            print(traceback.format_exc())
            logging.error('【大奖励任务领取】: 错误，原因为: ' + str(e)) 
 
