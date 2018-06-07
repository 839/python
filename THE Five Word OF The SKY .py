#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import random
import string


headers = {
'User-Agent':'Mozilla/5.0 (Linux; Android 5.1.1; Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044033 Mobile Safari/537.36 MicroMessenger/6.6.6.1300(0x26060637) NetType/WIFI Language/zh_CN',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,image/wxpic,image/sharpp,image/apng,*/*;q=0.8',
'Accept-Language':'zh-CN,en-US;q=0.8',
# 'Cookie':' OpenId=ofcL9wRNNN94gatHszUI7j7HLm2a; PHPSESSID=4r54n1se1rk3malsm3bvp7sqq3; XSRF-TOKEN=eyJpdiI6InVxTnhlT0ZcL1NaN0lcL3FZZHBKaVFRQT09IiwidmFsdWUiOiJmRHdpT1pMWG1PQzU1eUJcL0lWT1NUV0VEODkyajNjTGpRMExlRHZ1R1ptSlQ2NkQ1eGRwZmNteW1VUDRFYW9xSlZnNTRoTEwyeXRWZEtvUTVSNlNVV3c9PSIsIm1hYyI6Ijg1MDJmMWIxOWFlM2UyNGI3ZThhYTZlNTk0MmYwY2E2YWU0YTZiODFlNTgyMzk0NGM2ZTE1MWE3NjZkMDU5ZWQifQ%3D%3D; laravel_session=eyJpdiI6IkRkMlVBbWtFMDBzMVgwZU85Q0xoY3c9PSIsInZhbHVlIjoiWXgzUVNLcGd5STJKbmRzK1IxMWtwQkVJYzB2WXZzWjBpdkh4YndpQkU4Y1lid3llZ0ViVkttenlUczF0NEhnMVQzSlczSTg1WDA5d1BFSVduUktMalE9PSIsIm1hYyI6IjYyNTJlM2RhMWQwMzEzOGI2MjQwMGFkMzhkOGU0MTc5MWFmNjMyMGQ0YzMxMTlmNmJhYjlkMmJjYTJjMDA3YWIifQ%3D%3D'
}
# cookies={"PHPSESSID":"3ftd04p8jgs6nhdhakmqaf1vq2","laravel_session":"eyJpdiI6Ikt6R2lBaE1EZ3hIREwzRU00V3pFOXc9PSIsInZhbHVlIjoiQ1c3RE04RkxGXC9RdlRmSHE2VUVINXlLWHdrc1h4R25jT3d0UzNFUUxMWEJZckdGWmdFVkY3eXIybDZLbUI0elV1WXU5ZndiNTRqakxvOXNUZlpBSXBnPT0iLCJtYWMiOiI0ZmEzMTI3ZWFhMWIxYzdiODA5MTc1ZjZiMGY5MjY5OWIyNDZiNjM1N2ExYTcxZjBkMWFjNzFhNTQ3N2E1MDY3In0%","XSRF-TOKEN":"eyJpdiI6IngrUG5OU21OVFpaQ2ZuZ0ZpWWt1MEE9PSIsInZhbHVlIjoibzZSQXNcL1pEM3hZR2NaSlBzcERScjhlUm0zUVNHUDFMc3hLYlZ5MTlPdGFNdG9EUFNDXC9Ra2JqdzV5NmxydjRDOXJBZkxLeHp3S2t5OHc5VWxjXC85SlE9PSIsIm1hYyI6ImIzODBiNjAwMTVmZmNmNDQ4YmVhMGM4MjgwMTE1ZGEwYzczNThmMWE0MjQ1NTEyNjg5MzVkOGM5ZTRiMjIxOGQifQ"}
# list = ['a','b','c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]
nlist = ["0","1","2","3","4","5","6","7","8","9"]
str=string.ascii_lowercase+string.ascii_uppercase;
rlist = nlist + list(str)
random.shuffle(rlist)
slice = random.sample(rlist, 22)  #从list中随机获取5个元素，作为一个片断返回  
header = "ofcL9w"
id = header+''.join(slice)
cookies={"OpenId":id,"PHPSESSID":"3ftd04p8jgs6nhdhakmqaf1vq2","laravel_session":"eyJpdiI6Ikt6R2lBaE1EZ3hIREwzRU00V3pFOXc9PSIsInZhbHVlIjoiQ1c3RE04RkxGXC9RdlRmSHE2VUVINXlLWHdrc1h4R25jT3d0UzNFUUxMWEJZckdGWmdFVkY3eXIybDZLbUI0elV1WXU5ZndiNTRqakxvOXNUZlpBSXBnPT0iLCJtYWMiOiI0ZmEzMTI3ZWFhMWIxYzdiODA5MTc1ZjZiMGY5MjY5OWIyNDZiNjM1N2ExYTcxZjBkMWFjNzFhNTQ3N2E1MDY3In0%","XSRF-TOKEN":"eyJpdiI6IngrUG5OU21OVFpaQ2ZuZ0ZpWWt1MEE9PSIsInZhbHVlIjoibzZSQXNcL1pEM3hZR2NaSlBzcERScjhlUm0zUVNHUDFMc3hLYlZ5MTlPdGFNdG9EUFNDXC9Ra2JqdzV5NmxydjRDOXJBZkxLeHp3S2t5OHc5VWxjXC85SlE9PSIsIm1hYyI6ImIzODBiNjAwMTVmZmNmNDQ4YmVhMGM4MjgwMTE1ZGEwYzczNThmMWE0MjQ1NTEyNjg5MzVkOGM5ZTRiMjIxOGQifQ"}
id = raw_input("input_id:")
num = raw_input("input_num:")
url = 'http://erp.pingnuosoft.com/wap/marketing/middleHandlePage?u_id=%s&a_id=%s&from=singlemessage'%(id,num)
print url
# response = requests.get(url,headers = headers,cookies = cookies)

# 返回信息ofcL9wZtPqRiwQMRAOprDLU_lXb8
# print response.text
# 返回响应头
# print response.status_code