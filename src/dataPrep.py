import requests
import json
import base64
import os
import pathlib
import datetime

headers = {'Origin': 'https://app.cpcbccr.com'}
headers['Accept-Encoding'] ="gzip, deflate, br"
headers['Accept-Language'] ="en-GB,en-US;q=0.9,en;q=0.8"
headers['User-Agent'] ="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36"
headers['Content-Type'] ="application/x-www-form-urlencoded"
headers['Accept'] ="application/json, text/plain, */*"
headers['Referer'] ="https://app.cpcbccr.com/ccr/"
headers['Connection'] ="keep-alive"
headers['Host'] ="app.cpcbccr.com"

#encoded_data = "eyJkcmF3IjoxLCJjb2x1bW5zIjpbeyJkYXRhIjowLCJuYW1lIjoiIiwic2VhcmNoYWJsZSI6dHJ1ZSwib3JkZXJhYmxlIjpmYWxzZSwic2VhcmNoIjp7InZhbHVlIjoiIiwicmVnZXgiOmZhbHNlfX1dLCJvcmRlciI6W10sInN0YXJ0IjowLCJsZW5ndGgiOjUwLCJzZWFyY2giOnsidmFsdWUiOiIiLCJyZWdleCI6ZmFsc2V9LCJmaWx0ZXJzVG9BcHBseSI6eyJwYXJhbWV0ZXJfbGlzdCI6W3siaWQiOjcsIml0ZW1OYW1lIjoiUE0yLjUiLCJpdGVtVmFsdWUiOiJwYXJhbWV0ZXJfMTkzIn1dLCJjcml0ZXJpYSI6IjQgSG91cnMiLCJyZXBvcnRGb3JtYXQiOiJUYWJ1bGFyIiwiZnJvbURhdGUiOiIxNC0xMC0yMDE3IFQwMDowMDowMFoiLCJ0b0RhdGUiOiIyMi0xMC0yMDE3IFQwMDowMDowMFoiLCJzdGF0ZSI6IlV0dGFyIFByYWRlc2giLCJjaXR5IjoiS2FucHVyIiwic3RhdGlvbiI6InNpdGVfMjc2IiwicGFyYW1ldGVyIjpbInBhcmFtZXRlcl8xOTMiXSwicGFyYW1ldGVyTmFtZXMiOlsiUE0yLjUiXX0sInBhZ2luYXRpb24iOjF9"

f = open("delhi_anand_vihar.csv", "w")
f.write("state, city, station,fromDate, AT, BP, PM10, PM2.5, RH, SR,  Toluene, WD, WS, CO, Benzene, NH3, NO, NO2, NOx, Ozone, SO2\n") ### Column names


#Mumbai -1  , Navi Mumbai -2017
# Bangalore - 2/3 - 2017
# Delhi - 5 stations 2017
# 10 stations - which have data from 2017 to 2020.
####2017
stationList = [
				{"city":"Delhi", "station":"site_301", "state":"Delhi"},
			   ]

# #{"city": "Bengaluru", "station": "site_162", "state": "Karnataka"},
# 				{"city":"Bengaluru", "station":"site_163", "state":"Karnataka"},
# 				{"city": "Bengaluru", "station": "site_164", "state": "Karnataka"},
# 				{"city": "Bengaluru", "station": "site_165", "state": "Karnataka"},
# 				{"city": "Bengaluru", "station": "site_166", "state": "Karnataka"},
# 				{"city": "Aurangabad", "station": "site_198", "state": "Maharastra"},
# 				{"city": "Chandrapur", "station": "site_271", "state": "Maharastra"},
# 				{"city": "Chandrapur", "station": "site_295", "state": "Maharastra"},
# 				{"city": "Nagpur", "station": "site_303", "state": "Maharastra"},
# 				{"city": "Nashik", "station": "site_304", "state": "Maharastra"},
# 				{"city": "Navi Mumbai", "station": "site_261", "state": "Maharastra"},
# 				{"city": "Pune", "station": "site_292", "state": "Maharastra"},
# 				{"city": "Solapur", "station": "site_302", "state": "Maharastra"},
# 				{"city": "Thane", "station": "site_305", "state": "Maharastra"}



parentPath = str(pathlib.Path(__file__).parent.parent)
jsonTemplateFile = parentPath  + '/data/raw/requestTemplate.json'

staticFeatures = ["AT", "BP", "PM10", "PM2.5", "RH", "SR", "Toluene", "WD", "WS", "CO", "Benzene", "NH3", "NO", "NO2", "NOx", "Ozone", "SO2"]
dateCurrent = datetime.datetime.now()
date_time_str = '01-10-2017'
date_time_obj = datetime.datetime.strptime(date_time_str, '%d-%m-%Y')
print(date_time_obj.date())

dataTemplate = ""
with open(jsonTemplateFile, 'r') as fileTemplate:
	dataTemplate = fileTemplate.read().replace('\n', '')

for stationDict in stationList:
	while date_time_obj.date() < dateCurrent.date():
		newState ='"state": "' + stationDict['state'] +'"'
		newCity = '"city": "' + stationDict['city'] + '"'
		newStation='"station": "' + stationDict['station'] + '"'
		formatFrom = '"fromDate": "{} T00:00:00Z"'.format(date_time_obj.date().strftime('%d-%m-%Y'))
		date_time_obj_TO = date_time_obj + datetime.timedelta(days=1)
		formatTo = '"toDate": "{} T00:00:00Z"'.format(date_time_obj_TO.date().strftime('%d-%m-%Y'))
		d1 = dataTemplate.replace('"fromDate": "$$"', formatFrom)
		d2 = d1.replace('"toDate": "$$"', formatTo)
		date_time_obj = date_time_obj + datetime.timedelta(days=1)
		d3 = d2.replace('"state": "$$"',newState)
		d4 = d3.replace('"city": "$$"', newCity)
		d5 = d4.replace('"station": "$$"',newStation )
		print (d5)
		d5_bytes = d5.encode("utf-8")
		base64_bytes = base64.b64encode(d5_bytes)
		r = requests.post("https://app.cpcbccr.com/caaqms/fetch_table_data", headers=headers, data=base64_bytes,
						  verify=False)
		print(r.status_code)
		if r.status_code == 200:
			print("Response code 200")
			json_data = json.dumps(r.json())
			pjson=json.loads(json_data)
			print(pjson)
			arrBody = pjson['data']['tabularData']['bodyContent']
			stringCsv = ""
			for ele in arrBody:
				stringCsv  = ele['from date']
				for feature in staticFeatures:
					if feature in ele and ele[feature] is not None:
						stringCsv = stringCsv + "," + ele[feature]
					else:
						stringCsv = stringCsv + "," + "None"
				print(stringCsv)
				fullLine = stationDict['state'] + "," +  stationDict['city'] + "," + stationDict['station'] + "," + stringCsv + "\n"
				f.write( fullLine)
