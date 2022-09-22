import requests
import json

url = "https://api-v2.mlytics.co/mdns/v2/_internal/zone/"

payload = json.dumps({
  "org_id": "1001662431868",
  "zone": {
    "domain": "plat5892.com",
    "status": 1
  },
  "rrsets": []
})
headers = {
  'Content-Type': 'application/json',
  'X-CONSUMER-GROUPS': 'service',
  'apikey': 'jdc5KIs4Xa75u4vx7I5RqNSZCycJXZNv'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
