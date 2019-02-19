#!/usr/bin/python
import datetime
import time
import csv
import os
import requests
import time


cr = csv.reader(open('summary.csv','rU'))

next(cr)

for row in cr:
	date = (row[0])
	print (date)
	conv = time.strptime(date,"%d/%m/%Y")
	dateconv = (time.strftime("%m/%d/%Y",conv)) # converted new US date format from UK
	dateoutput = dateconv.replace("/", "%2F")
	print ('[+] Date:', dateoutput)
	amountfloat = (float(row[2])) 
	amount = amountfloat
	print ('[+] Amount:', amount)
	#print (type(amount))
	if amount > 0:
		print ('\t[-] Negitive number')
		expense = 'true'					
	else:
		print ('\t[-] Positive number')
		expense = 'false'					
	amount = str(amount)	
	memo = (row[3])
	merchant = memo.replace(" ", "%20").replace("*", "%2a").replace("/", "%2f").replace("\\", "%5c").replace("&", "%26").replace("?", "%3f").replace(".", "%2e") # urlcode for spaces

	catID = '0' 

	print ('[+] Merchant', merchant)

		###### Changing CATID Number ######
	if "SHOPPING" in memo:
		catID = '707'
		print ('[+] Catagory ID:', catID)

	elif "FAST FOOD" in memo:
		catID = '706'
		print ('[+] Catagory ID:', catID)

	else:
		catID = '20'
		print ('[+] Catagory ID:', catID)

	category = 'Uncategorized'
	print ('[+] Category:', category)
	mtIsExpense = expense
	print ('[+] Expense:', mtIsExpense)

	print ('\n\n')

	output = str(os.system("curl -i -s -k -X POST 'https://mint.intuit.com/updateTransaction.xevent' \
	-H 'Host: mint.intuit.com' \
	-H 'User-Agent: XXXXX' \
	-H 'Accept: */*' \
	-H 'Accept-Language: en-US,en;q=0.5' \
	--compressed \
	-H 'X-Requested-With: XMLHttpRequest' \
	-H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' \
	-H 'Referer: XXXXX' \
	-H 'Cookie: XXXXX' \
	-H 'Connection: close' \
	--data \
	'cashTxnType=on&mtCheckNo=&tagXXXX=0&tagXXXX=0&tagXXXX=0&tagXXXX=0&task=txnadd&txnId=%3A0&mtType=cash&mtAccount=XXXX&symbol=&note=&isInvestment=false&catId="+catID+"&category="+category+"&merchant="+merchant+"&date="+dateoutput+"&amount="+amount+"&mtIsExpense="+expense+"&mtCashSplitPref=2&token=XXXXX'"))

	print (catID, category, merchant, dateoutput, amount, expense)

	print (output)

	time.sleep(3)
	print ('\n\n===================\n')















