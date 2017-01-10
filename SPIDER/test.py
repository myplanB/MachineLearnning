#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/15 11:45
# @Author  : sonny
# @Site    : 
# @File    : test.py
# @Software: PyCharm
import urllib2
import urllib

def download(url,user_agent='wswp',num_retries=2):
	print "正在下载网页：\n"
	headers = {'User-agent':user_agent}
	request = urllib2.Request(url,headers=headers)
	try:
		html = urllib2.urlopen(request).read()
	except urllib2.URLError as e:
		print "下载失败：",e.reason
		html = ""
		if num_retries > 0:
			if hasattr(e,'code') and 500 <= e.code < 600:
				return download(url,user_agent,num_retries-1)
	return html

if __name__ == "__main__":
	print download("http://www.taobao.com")