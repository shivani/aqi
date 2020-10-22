import requests
import json
import base64
import os
import pathlib
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

f = open("allstations.csv", "w")
f.write("state, city, station,fromDate, AT, BP, PM10, PM2.5, RH, SR, Temp, Toluene, WD, WS, CO, Benzene,P-Xylene, NH3, NO, NO2, NOx, Ozone, SO2\n") ### Column names


#Mumbai -1  , Navi Mumbai -2017
# Bangalore - 2/3 - 2017
# Delhi - 5 stations 2017
# 10 stations - which have data from 2017 to 2020.
####2017
stationList = [
				{"city":"Delhi", "station":"site_301", "state":"Delhi"},
				{"city": "Bengaluru", "station": "site_162", "state": "Karnataka"},
				{"city":"Bengaluru", "station":"site_163", "state":"Karnataka"},
				{"city": "Bengaluru", "station": "site_164", "state": "Karnataka"},
				{"city": "Bengaluru", "station": "site_165", "state": "Karnataka"},
				{"city": "Bengaluru", "station": "site_166", "state": "Karnataka"},
				{"city": "Aurangabad", "station": "site_198", "state": "Maharastra"},
				{"city": "Chandrapur", "station": "site_271", "state": "Maharastra"},
				{"city": "Chandrapur", "station": "site_295", "state": "Maharastra"},
				{"city": "Nagpur", "station": "site_303", "state": "Maharastra"},
				{"city": "Nashik", "station": "site_304", "state": "Maharastra"},
				{"city": "Navi Mumbai", "station": "site_261", "state": "Maharastra"},
				{"city": "Pune", "station": "site_292", "state": "Maharastra"},
				{"city": "Solapur", "station": "site_302", "state": "Maharastra"},
				{"city": "Thane", "station": "site_305", "state": "Maharastra"}
			   ]

#Yamini to populate
###



parentPath = str(pathlib.Path(__file__).parent.parent)
jsonTemplateFile = parentPath  + '/data/raw/requestTemplate.json'

staticFeatures = ["AT", "BP", "PM10", "PM2.5", "RH", "SR", "Temp", "Toluene", "WD", "WS", "CO", "Benzene","Xylene", "NH3", "NO", "NO2", "NOx", "Ozone", "SO2"]
for stationDict in stationList:
	print(stationDict['state'])
	print(stationDict['city'])
	print(stationDict['station'])
	dataTemplate = ""
	with open(jsonTemplateFile, 'r') as fileTemplate:
		dataTemplate = fileTemplate.read().replace('\n', '')

	newState ='"state": "' + stationDict['state'] +'"'
	newCity = '"city": "' + stationDict['city'] + '"'
	newStation='"station": "' + stationDict['station'] + '"'

	d1 = dataTemplate.replace('"fromDate": "$$"', '"fromDate": "17-01-2018 T00:00:00Z"')
	d2 = d1.replace('"toDate": "$$"', '"toDate": "18-01-2018 T00:00:00Z"')
	d3 = d2.replace('"state": "$$"',newState)
	d4 = d3.replace('"city": "$$"', newCity)
	d5 = d4.replace('"station": "$$"',newStation )
	#print(d5)
	### template to be update above data.
	#d6='{"draw":1,"columns":[{"data":0,"name":"","searchable":true,"orderable":false,"search":{"value":"","regex":false}}],"order":[],"start":0,"length":50,"search":{"value":"","regex":false},"filtersToApply":{"parameter_list":[{"id":7,"itemName":"PM2.5","itemValue":"parameter_193"}],"criteria":"4 Hours","reportFormat":"Tabular","fromDate":"14-10-2017 T00:00:00Z","toDate":"22-10-2017 T00:00:00Z","state":"Uttar Pradesh","city":"Kanpur","station":"site_276","parameter":["parameter_193"],"parameterNames":["PM2.5"]},"pagination":1}'
	#d6='{"draw":1,"columns":[{"data":0,"name":"","searchable":true,"orderable":false,"search":{"value":"","regex":false}}],"order":[],"start":0,"length":50,"search":{"value":"","regex":false},"filtersToApply":{"parameter_list":[{"id":7,"itemName":"PM2.5","itemValue":"parameter_193"}],"criteria":"4 Hours","reportFormat":"Tabular","fromDate":"14-10-2020 T00:00:00Z","toDate":"15-10-2020 T00:00:00Z","state":"Delhi","city":"Delhi","station":"site_108","parameter":["parameter_193"],"parameterNames":["PM2.5"]},"pagination":1}'
	d5_bytes = d5.encode("utf-8")
	base64_bytes = base64.b64encode(d5_bytes)
	## Encoding here.
	#encoded_data1="ewogICAgImRyYXciOiAxLAogICAgImNvbHVtbnMiOiBbCiAgICAgICAgewogICAgICAgICAgICAiZGF0YSI6IDAsCiAgICAgICAgICAgICJuYW1lIjogIiIsCiAgICAgICAgICAgICJzZWFyY2hhYmxlIjogdHJ1ZSwKICAgICAgICAgICAgIm9yZGVyYWJsZSI6IGZhbHNlLAogICAgICAgICAgICAic2VhcmNoIjogewogICAgICAgICAgICAgICAgInZhbHVlIjogIiIsCiAgICAgICAgICAgICAgICAicmVnZXgiOiBmYWxzZQogICAgICAgICAgICB9CiAgICAgICAgfQogICAgXSwKICAgICJvcmRlciI6IFtdLAogICAgInN0YXJ0IjogMCwKICAgICJsZW5ndGgiOiA1MCwKICAgICJzZWFyY2giOiB7CiAgICAgICAgInZhbHVlIjogIiIsCiAgICAgICAgInJlZ2V4IjogZmFsc2UKICAgIH0sCiAgICAiZmlsdGVyc1RvQXBwbHkiOiB7CiAgICAgICAgCiAgICAgICAgImNyaXRlcmlhIjogIjQgSG91cnMiLAogICAgICAgICJyZXBvcnRGb3JtYXQiOiAiVGFidWxhciIsCiAgICAgICAgImZyb21EYXRlIjogIjIyLTEwLTIwMTcgVDAwOjAwOjAwWiIsCiAgICAgICAgInRvRGF0ZSI6ICIzMC0xMC0yMDE3IFQwMDowMDowMFoiLAogICAgICAgICJzdGF0ZSI6ICJEZWxoaSIsCiAgICAgICAgImNpdHkiOiAiRGVsaGkiLAogICAgICAgICJzdGF0aW9uIjogInNpdGVfMzAxIiwKICAgICAgICAicGFyYW1ldGVyIjpbInBhcmFtZXRlcl8yMDQiLCJwYXJhbWV0ZXJfMjM4IiwicGFyYW1ldGVyXzIxNSIsInBhcmFtZXRlcl8xOTMiLCJwYXJhbWV0ZXJfMjM1IiwicGFyYW1ldGVyXzIzNyIsInBhcmFtZXRlcl8xOTgiLCJwYXJhbWV0ZXJfMjMyIiwicGFyYW1ldGVyXzIzNCIsInBhcmFtZXRlcl8yMzMiLCJwYXJhbWV0ZXJfMjAzIiwicGFyYW1ldGVyXzIwMiIsInBhcmFtZXRlcl8zMjQiLCJwYXJhbWV0ZXJfMzExIiwicGFyYW1ldGVyXzIyNiIsInBhcmFtZXRlcl8xOTQiLCJwYXJhbWV0ZXJfMjI1IiwicGFyYW1ldGVyXzIyMiIsInBhcmFtZXRlcl8zMTIiXSAsCiAgICAgICAgInBhcmFtZXRlck5hbWVzIjogWyJBVCIsIkJQIiwiUE0xMCIsIlBNMi41IiwiUkgiLCJTUiIsIlRlbXAiLCJUb2x1ZW5lIiwiV0QiLCJXUyIsIkNPIiwiQmVuemVuZSIsIlAtWHlsZW5lIiwiTkgzIiwiTk8iLCJOTzIiLCJOT3giLCJPem9uZSIsIlNPMiJdCiAgICB9LAogICAgInBhZ2luYXRpb24iOiAxCn0="
	r = requests.post("https://app.cpcbccr.com/caaqms/fetch_table_data", headers=headers, data=base64_bytes,
					  verify=False)
	if r.status_code == 200:
		print("Response code 200")
		json_data = json.dumps(r.json())
		pjson=json.loads(json_data)
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

		#"state, city, station, AT, BP, PM10, PM2.5, RH, SR, Temp, Toluene, WD, WS, CO, Benzene,P-Xylene, NH3, NO, NO2, NOx, Ozone, SO2\n")  ### Column names


# ---> One person can check on duration and pagination fromDate=2017
###
###
#
#
	#
	#Creating csv for all JSON calls
#




	#json_data_hash = hashlib.md5(json_data)
	#row_exists['json_data'] = json_data
	#row_exists['json_data_hash'] = json_data_hash.hexdigest()
	#row_exists['status_code'] = r.status_code


#enc="eyJkcmF3IjoxLCJjb2x1bW5zIjpbeyJkYXRhIjowLCJuYW1lIjoiIiwic2VhcmNoYWJsZSI6dHJ1ZSwib3JkZXJhYmxlIjpmYWxzZSwic2VhcmNoIjp7InZhbHVlIjoiIiwicmVnZXgiOmZhbHNlfX1dLCJvcmRlciI6W10sInN0YXJ0IjowLCJsZW5ndGgiOjUwLCJzZWFyY2giOnsidmFsdWUiOiIiLCJyZWdleCI6ZmFsc2V9LCJmaWx0ZXJzVG9BcHBseSI6eyJwYXJhbWV0ZXJfbGlzdCI6W3siaWQiOjcsIml0ZW1OYW1lIjoiUE0yLjUiLCJpdGVtVmFsdWUiOiJwYXJhbWV0ZXJfMTkzIn1dLCJjcml0ZXJpYSI6IjQgSG91cnMiLCJyZXBvcnRGb3JtYXQiOiJUYWJ1bGFyIiwiZnJvbURhdGUiOiIxNC0xMC0yMDE3IFQwMDowMDowMFoiLCJ0b0RhdGUiOiIyMi0xMC0yMDE3IFQwMDowMDowMFoiLCJzdGF0ZSI6IlV0dGFyIFByYWRlc2giLCJjaXR5IjoiS2FucHVyIiwic3RhdGlvbiI6InNpdGVfMjc2IiwicGFyYW1ldGVyIjpbInBhcmFtZXRlcl8xOTMiXSwicGFyYW1ldGVyTmFtZXMiOlsiUE0yLjUiXX0sInBhZ2luYXRpb24iOjF9"