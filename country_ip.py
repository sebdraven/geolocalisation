#!/usr/bin/python
#Author: Sebdraven

import dschield
import sys


filetoload=sys.argv[1]

fr=open(filetoload,'r')
ds=dschield.dschield('http://dshield.org/ipinfo_ascii.html?ip=')
while 1:

	t=fr.readline()
	ip,country,asname=ds.response(t.strip())
	print ip +';'+country + ';'+asname
	
	
