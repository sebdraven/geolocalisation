#!/usr/bin/python


import dschield
import sys


filetoload=sys.argv[1]


ds=dschield.dschield('http://dshield.org/ipinfo_ascii.html?ip=')
with open(filetoload,'r') as fr:
    for t in fr:
	ip,country,asname=ds.response(t.strip())
	print ip +';'+country + ';'+asname
	
	
