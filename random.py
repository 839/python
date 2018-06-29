#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import string
import os
import requests
import random
import time
import datetime  
headers = {
'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8',
'Accept-Language':'zh-CN,en-US;q=0.8',
}
nlist = ["0","1","2","3","4","5","6","7","8","9"]
str=string.ascii_lowercase+string.ascii_uppercase;
rlist = nlist + list(str)
header = "ofcL9w"
rlist = []
def createRandomStr(file_no):
    file = open(file_no,'w')
    for i in range(1,100):
        random.shuffle(rlist)
        slice = random.sample(rlist,22)
        rand_str = header + ''.join(slice) + '\n'
        rlist.append(rand_str)
        file.write(rand_str)
    file.close()

def readRandomStr(file_no):
    if os.path.exists(file_no):
        file = open(file_no,'r')
        for line in file:
            rlist.append(line.replace('\n',''))
        file.close()
    else:
        createRandomStr(file_no)       

if __name__ == '__main__':
    file_no = raw_input('input_no:')
    count = raw_input('input_count(1~100):')
    aid  =  raw_input('input_article:')
    readRandomStr(file_no)
    i = 0
    for ssid in rlist:
        if i < count:
            ssid = ''.join(ssid).replace('\n','')
            cookies={"OpenId":ssid,"PHPSESSID":"3ftd04p8jgs6nhdhakmqaf1vq2","laravel_session":"eyJpdiI6Ikt6R2lBaE1EZ3hIREwzRU00V3pFOXc9PSIsInZhbHVlIjoiQ1c3RE04RkxGXC9RdlRmSHE2VUVINXlLWHdrc1h4R25jT3d0UzNFUUxMWEJZckdGWmdFVkY3eXIybDZLbUI0elV1WXU5ZndiNTRqakxvOXNUZlpBSXBnPT0iLCJtYWMiOiI0ZmEzMTI3ZWFhMWIxYzdiODA5MTc1ZjZiMGY5MjY5OWIyNDZiNjM1N2ExYTcxZjBkMWFjNzFhNTQ3N2E1MDY3In0%","XSRF-TOKEN":"eyJpdiI6IngrUG5OU21OVFpaQ2ZuZ0ZpWWt1MEE9PSIsInZhbHVlIjoibzZSQXNcL1pEM3hZR2NaSlBzcERScjhlUm0zUVNHUDFMc3hLYlZ5MTlPdGFNdG9EUFNDXC9Ra2JqdzV5NmxydjRDOXJBZkxLeHp3S2t5OHc5VWxjXC85SlE9PSIsIm1hYyI6ImIzODBiNjAwMTVmZmNmNDQ4YmVhMGM4MjgwMTE1ZGEwYzczNThmMWE0MjQ1NTEyNjg5MzVkOGM5ZTRiMjIxOGQifQ"}
            url = 'http://erp.pingnuosoft.com/wap/marketing/middleHandlePage?u_id=%s&a_id=%s&from=singlemessage'%(file_no,aid)
            response = requests.get(url,headers = headers,cookies = cookies)
            t = random.randint(1,4)*30
            print(t)
            time.sleep(t)
            print(datetime.datetime.now())
            i += 1
        else:
            print('ok!')
            break
        