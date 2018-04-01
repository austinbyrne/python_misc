#!/usr/bin/env python3

import requests
import json

# for auth below go to https://developer.domain.com.au/io-docs
headers = {'authorization': 'Bearer <----YOUR ACCESS TOKEN HERE--->,'content-type': 'application/json'}
url = 'https://api.domain.com.au/v1/listings/residential/_search'
payload = {
    "listingType":"Rent"
    ,"maxBedrooms":3
    ,"page":1 # TODO: loop through pages
    ,"pageSize":10 # default max
    ,"locations":[
        {"state":"NSW"
        ,"region":""
        ,"area":"Northern Beaches"
        ,"suburb":"Manly"
        ,"postCode":""
        ,"includeSurroundingSuburbs":True
        }
    ]
    ,"propertyFeatures":[
    "WaterViews"
    ,"AirConditioning"
    ]
}

r = requests.post(url,headers=headers,data=json.dumps(payload))

parsed_json = json.loads(r.text)

for i in parsed_json:
    print("https://www.domain.com.au/" + str(i['listing']['id']))
