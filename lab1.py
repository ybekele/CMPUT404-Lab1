#!/usr/bin/env python

import requests 

r = requests.get("http://www.google.com")
print(r.status_code)
print(r.text)
#print("version = " )
#print(requests.__version__)
a = requests.get("https://raw.githubusercontent.com/ybekele/CMPUT404-Lab1/master/lab1.py")
print(a.text)
