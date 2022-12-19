import random
from pystyle import *
from atexit import register
from time import sleep
import os,json,re,sys
import threading,base64
import os,time,re,json,random
from datetime import datetime
from time import sleep,strftime
import requests

Array_Anh = [
"https://khangdztool.000webhostapp.com/anh/1.jpeg",
"https://khangdztool.000webhostapp.com/anh/2.jpeg",
"https://khangdztool.000webhostapp.com/anh/3.jpeg",
"https://khangdztool.000webhostapp.com/anh/3.jpeg",
"https://khangdztool.000webhostapp.com/anh/4.jpeg",
"https://khangdztool.000webhostapp.com/anh/5.jpeg",
"https://khangdztool.000webhostapp.com/anh/6.jpeg",
"https://khangdztool.000webhostapp.com/anh/7.jpeg",
"https://khangdztool.000webhostapp.com/anh/8.jpeg",
"https://khangdztool.000webhostapp.com/anh/9.jpeg",
"https://khangdztool.000webhostapp.com/anh/10.jpeg",
"https://khangdztool.000webhostapp.com/anh/11.jpeg",
"https://khangdztool.000webhostapp.com/anh/12.jpeg",
"https://khangdztool.000webhostapp.com/anh/13.jpeg",
"https://khangdztool.000webhostapp.com/anh/14.jpeg",
"https://khangdztool.000webhostapp.com/anh/15.jpeg",
"https://khangdztool.000webhostapp.com/anh/16.jpeg",
"https://khangdztool.000webhostapp.com/anh/17.jpeg",
"https://khangdztool.000webhostapp.com/anh/18.jpeg",
"https://khangdztool.000webhostapp.com/anh/20.jpeg",
"https://khangdztool.000webhostapp.com/anh/21.jpeg",
"https://khangdztool.000webhostapp.com/anh/22.jpeg",
"https://khangdztool.000webhostapp.com/anh/23.jpeg",
"https://khangdztool.000webhostapp.com/anh/24.jpeg",
"https://khangdztool.000webhostapp.com/anh/25.jpeg",
"https://khangdztool.000webhostapp.com/anh/26.jpeg",
"https://khangdztool.000webhostapp.com/anh/28.jpeg",
"https://khangdztool.000webhostapp.com/anh/29.jpeg",
"https://khangdztool.000webhostapp.com/anh/30.jpeg",
"https://khangdztool.000webhostapp.com/anh/31.jpeg",
"https://khangdztool.000webhostapp.com/anh/32.jpeg",
"https://khangdztool.000webhostapp.com/anh/33.jpeg",
"https://khangdztool.000webhostapp.com/anh/34.jpeg",
"https://khangdztool.000webhostapp.com/anh/35.jpeg",
"https://khangdztool.000webhostapp.com/anh/36.jpeg",
"https://khangdztool.000webhostapp.com/anh/37.jpeg",
"https://khangdztool.000webhostapp.com/anh/38.jpeg",
"https://khangdztool.000webhostapp.com/anh/39.jpeg",
"https://khangdztool.000webhostapp.com/anh/40.jpeg",
"https://khangdztool.000webhostapp.com/anh/41.jpeg",
"https://khangdztool.000webhostapp.com/anh/42.jpeg",
"https://khangdztool.000webhostapp.com/anh/43.jpeg",
"https://khangdztool.000webhostapp.com/anh/44.jpeg",
"https://khangdztool.000webhostapp.com/anh/45.jpeg",
"https://khangdztool.000webhostapp.com/anh/46.jpeg",
"https://khangdztool.000webhostapp.com/anh/47.jpeg",
"https://khangdztool.000webhostapp.com/anh/48.jpeg",
"https://khangdztool.000webhostapp.com/anh/49.jpeg",
"https://khangdztool.000webhostapp.com/anh/50.jpeg",
"https://khangdztool.000webhostapp.com/anh/51.jpeg",
"https://khangdztool.000webhostapp.com/anh/52.jpeg",
"https://khangdztool.000webhostapp.com/anh/53.jpeg",
"https://khangdztool.000webhostapp.com/anh/54.jpeg",
"https://khangdztool.000webhostapp.com/anh/55.jpeg",
"https://khangdztool.000webhostapp.com/anh/56.jpeg",
"https://khangdztool.000webhostapp.com/anh/57.jpeg",
"https://khangdztool.000webhostapp.com/anh/58.jpeg",
"https://khangdztool.000webhostapp.com/anh/59.jpeg",
"https://khangdztool.000webhostapp.com/anh/60.jpeg",
"https://khangdztool.000webhostapp.com/anh/61.jpeg",
"https://khangdztool.000webhostapp.com/anh/62.jpeg",
"https://khangdztool.000webhostapp.com/anh/63.jpeg",
"https://khangdztool.000webhostapp.com/anh/64.jpeg",
"https://khangdztool.000webhostapp.com/anh/65.jpeg",
"https://khangdztool.000webhostapp.com/anh/66.jpeg",
"https://khangdztool.000webhostapp.com/anh/67.jpeg",
"https://khangdztool.000webhostapp.com/anh/68.jpeg",
"https://khangdztool.000webhostapp.com/anh/69.jpeg",
"https://khangdztool.000webhostapp.com/anh/70.jpeg",
"https://khangdztool.000webhostapp.com/anh/71.jpeg",
"https://khangdztool.000webhostapp.com/anh/72.jpeg",
"https://khangdztool.000webhostapp.com/anh/73.jpeg",
"https://khangdztool.000webhostapp.com/anh/74.jpeg",
"https://khangdztool.000webhostapp.com/anh/75.jpeg",
"https://khangdztool.000webhostapp.com/anh/76.jpeg",
"https://khangdztool.000webhostapp.com/anh/77.jpeg",
"https://khangdztool.000webhostapp.com/anh/78.jpeg",
"https://khangdztool.000webhostapp.com/anh/79.jpeg",
"https://khangdztool.000webhostapp.com/anh/80.jpeg",
"https://khangdztool.000webhostapp.com/anh/81.jpeg",
"https://khangdztool.000webhostapp.com/anh/82.jpeg",
"https://khangdztool.000webhostapp.com/anh/83.jpeg",
"https://khangdztool.000webhostapp.com/anh/84.jpeg",
"https://khangdztool.000webhostapp.com/anh/85.jpeg",
"https://khangdztool.000webhostapp.com/anh/86.jpeg",
"https://khangdztool.000webhostapp.com/anh/87.jpeg",
"https://khangdztool.000webhostapp.com/anh/88.jpeg",
"https://khangdztool.000webhostapp.com/anh/89.jpeg",
"https://khangdztool.000webhostapp.com/anh/90.jpeg",
"https://khangdztool.000webhostapp.com/anh/91.jpeg",
"https://khangdztool.000webhostapp.com/anh/92.jpeg",
"https://khangdztool.000webhostapp.com/anh/93.jpeg",
"https://khangdztool.000webhostapp.com/anh/94.jpeg",
"https://khangdztool.000webhostapp.com/anh/95.jpeg",
"https://khangdztool.000webhostapp.com/anh/96.jpeg",
"https://khangdztool.000webhostapp.com/anh/97.jpeg",
"https://khangdztool.000webhostapp.com/anh/98.jpeg",
"https://khangdztool.000webhostapp.com/anh/99.jpeg",
"https://khangdztool.000webhostapp.com/anh/100.jpeg",
"https://khangdztool.000webhostapp.com/anh/101.jpeg",
"https://khangdztool.000webhostapp.com/anh/102.jpeg",
"https://khangdztool.000webhostapp.com/anh/103.jpeg",
"https://khangdztool.000webhostapp.com/anh/104.jpeg",
"https://khangdztool.000webhostapp.com/anh/105.jpeg",
"https://khangdztool.000webhostapp.com/anh/106.jpeg",
"https://khangdztool.000webhostapp.com/anh/107.jpeg",
"https://khangdztool.000webhostapp.com/anh/108.jpeg",
"https://khangdztool.000webhostapp.com/anh/109.jpeg",
"https://khangdztool.000webhostapp.com/anh/110.jpeg",
"https://khangdztool.000webhostapp.com/anh/111.jpeg",
"https://khangdztool.000webhostapp.com/anh/112.jpeg",
"https://khangdztool.000webhostapp.com/anh/113.jpeg",
"https://khangdztool.000webhostapp.com/anh/114.jpeg",
"https://khangdztool.000webhostapp.com/anh/115.jpeg",
"https://khangdztool.000webhostapp.com/anh/116.jpeg",
"https://khangdztool.000webhostapp.com/anh/117.jpeg",
"https://khangdztool.000webhostapp.com/anh/118.jpeg",
"https://khangdztool.000webhostapp.com/anh/119.jpeg",
"https://khangdztool.000webhostapp.com/anh/120.jpeg",
"https://khangdztool.000webhostapp.com/anh/121.jpeg",
"https://khangdztool.000webhostapp.com/anh/122.jpeg",
"https://khangdztool.000webhostapp.com/anh/123.jpeg",
"https://khangdztool.000webhostapp.com/anh/124.jpeg",
"https://khangdztool.000webhostapp.com/anh/125.jpeg",
"https://khangdztool.000webhostapp.com/anh/126.jpeg",
"https://khangdztool.000webhostapp.com/anh/127.jpeg",
"https://khangdztool.000webhostapp.com/anh/128.jpeg",
"https://khangdztool.000webhostapp.com/anh/129.jpeg",
"https://khangdztool.000webhostapp.com/anh/130.jpeg",
"https://khangdztool.000webhostapp.com/anh/131.jpeg",
"https://khangdztool.000webhostapp.com/anh/132.jpeg",
"https://khangdztool.000webhostapp.com/anh/133.jpeg",
"https://khangdztool.000webhostapp.com/anh/134.jpeg",
"https://khangdztool.000webhostapp.com/anh/135.jpeg",
"https://khangdztool.000webhostapp.com/anh/136.jpeg",
"https://khangdztool.000webhostapp.com/anh/137.jpeg",
"https://khangdztool.000webhostapp.com/anh/138.jpeg",
"https://khangdztool.000webhostapp.com/anh/139.jpeg",
"https://khangdztool.000webhostapp.com/anh/140.jpeg",
"https://khangdztool.000webhostapp.com/anh/141.jpeg",
"https://khangdztool.000webhostapp.com/anh/142.jpeg",
"https://khangdztool.000webhostapp.com/anh/143.jpeg",
"https://khangdztool.000webhostapp.com/anh/144.jpeg",
"https://khangdztool.000webhostapp.com/anh/145.jpeg",
"https://khangdztool.000webhostapp.com/anh/146.jpeg",
"https://khangdztool.000webhostapp.com/anh/147.jpeg",
"https://khangdztool.000webhostapp.com/anh/148.jpeg",
"https://khangdztool.000webhostapp.com/anh/149.jpeg",
"https://khangdztool.000webhostapp.com/anh/150.jpeg",
"https://khangdztool.000webhostapp.com/anh/151.jpeg",
"https://khangdztool.000webhostapp.com/anh/152.jpeg",
"https://khangdztool.000webhostapp.com/anh/153.jpeg",
"https://khangdztool.000webhostapp.com/anh/154.jpeg",
"https://khangdztool.000webhostapp.com/anh/155.jpeg",
"https://khangdztool.000webhostapp.com/anh/156.jpeg",
"https://khangdztool.000webhostapp.com/anh/157.jpeg",
"https://khangdztool.000webhostapp.com/anh/158.jpeg",
"https://khangdztool.000webhostapp.com/anh/159.jpeg",
"https://khangdztool.000webhostapp.com/anh/160.jpeg",
"https://khangdztool.000webhostapp.com/anh/161.jpeg",
"https://khangdztool.000webhostapp.com/anh/162.jpeg",
"https://khangdztool.000webhostapp.com/anh/163.jpeg",
]
def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()
dau="\033[1;32m~ [✓] => "


    
class reg_pro5():
	def __init__(self,cookies, name) -> None:
		self.cookies = cookies
		self._id = self.cookies.split('c_user=')[1].split(';')[0]
		self.name = name
		headers = {
		'authority': 'www.facebook.com',
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
	    'accept-language': 'vi',
	    'cookie': self.cookies,
	    'sec-ch-prefers-color-scheme': 'light',
	    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
	    'sec-ch-ua-mobile': '?0',
	    'sec-ch-ua-platform': '"Windows"',
	    'sec-fetch-dest': 'document',
	    'sec-fetch-mode': 'navigate',
	    'sec-fetch-site': 'none',
	    'sec-fetch-user': '?1',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
	    'viewport-width': '1366',
		}
		url = requests.get('https://www.facebook.com/me', headers=headers).url
		profile = requests.get(url, headers=headers).text
		try:
			self.fb_dtsg = profile.split('{"name":"fb_dtsg","value":"')[1].split('"},')[0]
		except:
			self.fb_dtsg = profile.split(',"f":"')[1].split('","l":null}')[0]
	def Reg(self):
		headers = {
		'authority': 'www.facebook.com',
		'accept': '*/*',
		'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
		'cookie': self.cookies,
		'origin': 'https://www.facebook.com',
		'referer': 'https://www.facebook.com/pages/creation?ref_type=launch_point',
		'sec-ch-prefers-color-scheme': 'dark',
		'sec-ch-ua-mobile': '?0',
		'sec-ch-ua-platform': '"Windows"',
		'sec-fetch-dest': 'empty',
		'sec-fetch-mode': 'cors',
		'sec-fetch-site': 'same-origin',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
		'viewport-width': '979',
		'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
		'x-fb-lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
		}
		data = {
		'av': self._id,
		'__user': self._id,
		'__a': '1',
		'__dyn': '7AzHxq1mxu1syUbFuC0BVU98nwgU29zEdEc8co5S3O2S7o11Ue8hw6vwb-q7oc81xoswIwuo886C11xmfz81sbzoaEnxO0Bo7O2l2Utwwwi831wiEjwZwlo5qfK6E7e58jwGzE8FU5e7oqBwJK2W5olwuEjUlDw-wUws9ovUaU3qxWm2Sq2-azo2NwkQ0z8c84K2e3u362-2B0oobo',
		'__csr': 'gP4ZAN2d-hbbRmLObkZO8LvRcXWVvth9d9GGXKSiLCqqr9qEzGTozAXiCgyBhbHrRG8VkQm8GFAfy94bJ7xeufz8jK8yGVVEgx-7oiwxypqCwgF88rzKV8y2O4ocUak4UpDxu3x1K4opAUrwGx63J0Lw-wa90eG18wkE7y14w4hw6Bw2-o069W00CSE0PW06aU02Z3wjU6i0btw3TE1wE5u',
		'__req': 't',
		'__hs': '19296.HYP:comet_pkg.2.1.0.2.1',
		'dpr': '1',
		'__ccg': 'EXCELLENT',
		'__rev': '1006496476',
		'__s': '1gapab:y4xv3f:2hb4os',
		'__hsi': '7160573037096492689',
		'__comet_req': '15',
		'fb_dtsg': self.fb_dtsg,
		'jazoest': '25404',
		'lsd': 'ZM7FAk6cuRcUp3imwqvHTY',
		'__aaid': '800444344545377',
		'__spin_r': '1006496476',
		'__spin_b': 'trunk',
		'__spin_t': '1667200829',
		'fb_api_caller_class': 'RelayModern',
		'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
		'variables': '{"input":{"bio":"","categories":["181475575221097"],"creation_source":"comet","name":"'+self.name+'","page_referrer":"launch_point","actor_id":"'+self._id+'","client_mutation_id":"1"}}',
		'server_timestamps': 'true',
		'doc_id': '5903223909690825',
		}
		rp = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
		return rp
clear()
listCookie = []
def inputCooki():
    for x in range(10000000):
        cookies = input(Col.purple + "{" + Col.reset + str(x+1) + Col.purple + "}" + Col.reset + " Nhập Cookies " + Col.purple + "[" + Col.reset + "Bỏ Trống Ấn " + Col.blue + "Enter" + Col.reset + " Để Dừng" + Col.purple + "]" + Col.reset + " -> ")
        if cookies == "" or len(cookies) <= 20:
            break
        listCookie.append(cookies)
        with open("cookie.txt", "w") as f:
            f.write("\n".join(listCookie))
try:
    for ck in open("cookie.txt", "r+", encoding="utf-8-sig").read().split("\n"):
        if len(ck) >= 20:
            listCookie.append(ck)
except:
    inputCooki()
    if listCookie == []:
        inputCooki()
dem = 0
dl = input('\033[1;32m~ \033[1;37m[\033[1;31m+\033[1;37m] => \033[1;33mDelay Reg Pro5: \033[1;37m')
def delay(dl):
   for ti in range(int(dl) , 0, -1):
        print(dau,f'\033[1;31m◈ Delay Reg Pro5 > {ti} <   ',end='\r')
        sleep(0.200)
        print(dau,f'\033[1;32m◈ Delay Reg Pro5 > {ti} <   ',end='\r')
        sleep(0.200)
        print(dau,f'\033[1;33m◈ Delay Reg Pro5 > {ti} <   ',end='\r')
        sleep(0.200)
        print(dau,f'\033[1;35m◈ Delay Reg Pro5 > {ti} <   ',end='\r')
        sleep(0.200)
        print(dau,f'\033[1;36m◈ Delay Reg Pro5 > {ti} <   ',end='\r')
        sleep(0.200)
dem = 0
for i in range (1):
	for ck in listCookie:
		cookies = (ck)
		cookie = cookies
		i = 0
		# try:
		while True:
			print("Đang tiến hành reg page Pro5 vui lòng chờ....")
			gender = random.choice(["male", "female"])
			name = requests.get("https://story-shack-cdn-v2.glitch.me/generators/vietnamese-name-generator/").json()["data"][gender]
			link = random.choice(Array_Anh)
			__start = time.time()
			reg = reg_pro5(cookies, name).Reg()
			print("Tiến hành up avt page Pro5")
			if "id" in reg.text:
				id = reg.json()["data"]["additional_profile_plus_create"]["additional_profile"]["id"]
				up = requests.get(url="https://khangdztool.000webhostapp.com/avt.php?id="+id+"&link="+link+"&cookie="+cookie)
				if "Link Ảnh Có Vấn đề" in up.text:
					print("link ảnh Không ổn rồi")
				else:
					print("up avt thành công")
				print(id+"|"+name)
			else:
				print(reg.json())
			delay(dl)
			i+=1
			if i == 3:
				print("-"*100)
				break
		# except: 	
		# 	print("loi roi")


