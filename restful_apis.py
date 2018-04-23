import requests
import json

url = 'http://restmithil.triphobo.com/adda_list?p=0-1'
data = '''{
    "data":{
        "source":"factual_itinerary","status":"activate","creation_date_from":"2018-01-28","creation_date_to":"2018-01-29"
    },
    "action":"listing",
    "fields":["name","slug","slug_id","source"],
    "getCount":"yes"
}'''
response = requests.post(url, data=data)
print(response.text)

