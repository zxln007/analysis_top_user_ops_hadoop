#!/bin/python

import urllib2
import json
from datetime import datetime


namenode_jmx = urllib2.urlopen("http://namenode2-prd3.cnsuning.com:50070/jmx")
text = json.loads(namenode_jmx.read())
TopUserOpCounts_tmp = text["beans"][21]["TopUserOpCounts"] #unicode
text2 = json.loads(TopUserOpCounts_tmp)
TopUserOpCounts = text2["windows"][2]["ops"]  #list

time = datetime.now()
with open ("TopUserOpCounts","w") as f:
	f.write(str(time)+"\n")
	for item in TopUserOpCounts:
    		f.write(item.keys()[1]+ ':'+item.values()[1]+'\t'+str(item.keys()[0])+ ':'+str(item.values()[0])+"\n")
    		topUsers_keys = (item.keys()[2])
    		topUsers_value = (item.values()[2])
    		f.write(topUsers_keys+':\n')
    		for ops in  topUsers_value:
            		f.write("\t"+"count:"+str(ops["count"])+"\t"+"user:"+ops["user"]+"\n")
    		f.write("\n")
f.close()
