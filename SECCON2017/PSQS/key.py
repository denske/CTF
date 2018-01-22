#!/usr/bin/env python
#coding:utf-8

import sys

f1 = open(sys.argv[1])
PubKey = f1.read()
f1.close()
PubKey1 = PubKey.replace(" ","")
PubKey2 = PubKey1.replace(":","")
PubKey3 = PubKey2.replace("\n","")
PubKey4 = PubKey3.replace("\r","")
PubKey5 = PubKey4.replace("\t","").replace("\v","")
PubKey5.upper()
print PubKey5

f2 = open("data2.txt",'w')
f2.write(PubKey5)
f2.close()
