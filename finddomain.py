#!/usr/bin/python3

from whois import whois
import pandas as pd

name_of_domain = input("Enter the name of domain: ")

for line in whois(name_of_domain).text.splitlines():
	if "Registry Expiry Date" in line:
		final_split2 = line.split()[3].split("T")[0]
		print ("Expiry Date %s" %final_split2)
		if (pd.to_datetime(final_split2) - pd.to_datetime('today')).days <= 30:
			print ("Due for renewal")
		else:
			print ("Days to expire: %s" % (pd.to_datetime(final_split2) - pd.to_datetime('today')).days)

for line in whois(name_of_domain).text.splitlines():
	if "Registrant Organization" in line:
		print (line)

for line in whois(name_of_domain).text.splitlines():
	if "Registrant State/Province:" in line:
		print (line)

for line in whois(name_of_domain).text.splitlines():
	if "Registrant Country" in line:
		print (line)			
