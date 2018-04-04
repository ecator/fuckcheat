#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

from urllib.parse import quote
from urllib.parse import unquote

def XOR(str,pw):
	pwLen=len(pw)
	re=""
	for i in range(len(str)):
		re+=chr(ord(str[i]) ^ ord(pw[i%pwLen]))
	return re

def encodeURI(uri):
	return quote(uri)
def decodeURI(uri):
	return unquote(uri)


if __name__ == '__main__':
	str="骗子死全家"
	pw="bc3eaefd79993e3b92401aa6cf9f81f4"
	print(str,XOR(str,pw))
	uri="骗子死全家"
	print(uri,encodeURI(uri))