# -*- coding: UTF-8 -*-
import requests
import random
import string
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
id = input("input_id:")
num1 = int(input("input_startnum:"))
num2 = int(input("input_endtnum:"))
print(datetime.datetime.now())
while num1 <= num2:
        random.shuffle(rlist)
        slice = random.sample(rlist,22)
        openid = header+''.join(slice)
        cookies={"OpenId":openid,"PHPSESSID":"3ftd04p8jgs6nhdhakmqaf1vq2","laravel_session":"eyJpdiI6Ikt6R2lBaE1EZ3hIREwzRU00V3pFOXc9PSIsInZhbHVlIjoiQ1c3RE04RkxGXC9RdlRmSHE2VUVINXlLWHdrc1h4R25jT3d0UzNFUUxMWEJZckdGWmdFVkY3eXIybDZLbUI0elV1WXU5ZndiNTRqakxvOXNUZlpBSXBnPT0iLCJtYWMiOiI0ZmEzMTI3ZWFhMWIxYzdiODA5MTc1ZjZiMGY5MjY5OWIyNDZiNjM1N2ExYTcxZjBkMWFjNzFhNTQ3N2E1MDY3In0%","XSRF-TOKEN":"eyJpdiI6IngrUG5OU21OVFpaQ2ZuZ0ZpWWt1MEE9PSIsInZhbHVlIjoibzZSQXNcL1pEM3hZR2NaSlBzcERScjhlUm0zUVNHUDFMc3hLYlZ5MTlPdGFNdG9EUFNDXC9Ra2JqdzV5NmxydjRDOXJBZkxLeHp3S2t5OHc5VWxjXC85SlE9PSIsIm1hYyI6ImIzODBiNjAwMTVmZmNmNDQ4YmVhMGM4MjgwMTE1ZGEwYzczNThmMWE0MjQ1NTEyNjg5MzVkOGM5ZTRiMjIxOGQifQ"}
        url = 'http://erp.pingnuosoft.com/wap/marketing/middleHandlePage?u_id=%s&a_id=%s&from=singlemessage'%(id,num1)
        num1 += 1
        response = requests.get(url,headers = headers,cookies = cookies)
        t = random.randint(1,10)*30
        print(t)
        time.sleep(t)
        print(datetime.datetime.now())
