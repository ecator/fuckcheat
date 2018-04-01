#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import fuckcheat
import time
import random

def main():
	pass
	while True:
		pass
		mail=fuckcheat.mkmail(random.randint(10,30))
		pw=fuckcheat.mkpw(random.randint(10,15))
		if fuckcheat.fuckcheat(mail,pw):
			print("%s: %s ok"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),mail))
		else:
			print("%s: %s ng"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),mail))


if __name__ == '__main__':
	main()