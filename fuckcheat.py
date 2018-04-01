#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import time
import random

def fuckcheat(mail,pw):
	req=requests.Session()
	#初始化一个会话
	r=req.get("http://www.icloud.ios.itacnes.cn/index_dnbcn.asp")
	#登录
	postdatas={"wu":mail,"wp":pw,"x":"14","y":"18"}
	r=req.post("http://www.icloud.ios.itacnes.cn/ht/save.asp",data=postdatas)
	#上传设备验证信息
	postdatas="xqq=20180101&wt2=13012345682&wt1=iphonex&wt3=123456&q=&w=&%CC%E1%BD%BB=%BC%CC%D0%F8"
	r=req.post("http://www.icloud.ios.itacnes.cn/ht/savea.asp",data=postdatas)
	#上传认证问题:素质三连
	postdatas="dna_answer_1=%C4%E3%D0%A1%CA%B1%BA%F2%D7%EE%CF%B2%BB%B6%C4%C4%D2%BB%B1%BE%CA%E9%A3%BF&dna_answer_1=%B2%DD%C4%E3%C2%E8%B1%C6&dna_answer_2=%C4%E3%B5%C4%B5%DA%D2%BB%B8%F6%C9%CF%CB%BE%BD%D0%CA%B2%C3%B4%C3%FB%D7%D6%A3%BF&dna_answer_2=%B2%D9%C4%E3%C2%E8&dna_answer_3=%C4%E3%C9%CF%D0%A1%D1%A7%CA%B1%D7%EE%CF%B2%BB%B6%B5%C4%C0%CF%CA%A6%D0%D5%CA%B2%C3%B4%A3%BF&dna_answer_3=%C6%AD%D7%D3%CB%C0%C8%AB%BC%D2&%CC%E1%BD%BB=%BC%CC%D0%F8"
	r=req.post("http://www.icloud.ios.itacnes.cn/ht/saveb.asp",data=postdatas)
	
	if r.text.find("XOR(strV,strPass)")>=0:
		return True
	else:
		return False
			

#获取0-9,A-Z,a-z的list
def getrandchars():
	chars=list()
	for c in range(48,58):
		chars.append(chr(c))
	for c in range(65,91):
		chars.append(chr(c))
	for c in range(97,123):
		chars.append(chr(c))
	return chars

#随机生成邮箱
def mkmail(len=10,domain="icloud.com"):
	r=""
	i=0
	while i<len:
		pass
		i+=1
		r+=random.choice(getrandchars())
	return r+"@"+domain

#随机生成密码
def mkpw(len=10):
	r=""
	i=0
	while i<len:
		pass
		i+=1
		r+=random.choice(getrandchars())
	return r

if __name__ =="__main__":
	mail=mkmail(random.randint(10,30))
	pw=mkpw(random.randint(10,15))
	if fuckcheat(mail,pw):
		print("%s: %s ok"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),mail))
	else:
		print("%s: %s ng"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),mail))

