import json
import random
import requests
import string


def send_req():
    url = "https://api-v2.mlytics.co/mdns/v2/_internal/zone/"
    name = ''.join(random.sample((string.digits + string.ascii_lowercase), 4))
    domain = "plat5892.com"

    payload = json.dumps({
        "org_id": "1001662431868",
        "zone": {
            "zone_id": "2154cd45-6aa2-4444-9e78-f4a7efe774a8",
            "domain": domain,
            "status": 1
        },
        "rrsets": [
            {
                "name": name + "." + domain,
                "type": "CNAME",
                "ttl": 120,
                "proxied": False,
                "detail": [
                    {
                        "value": "testfire.net"
                    }
                ]
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json',
        'X-CONSUMER-GROUPS': 'service',
        'apikey': 'jdc5KIs4Xa75u4vx7I5RqNSZCycJXZNv'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


if __name__ == '__main__':
    for i in range(91):
        send_req()
        print(i)
