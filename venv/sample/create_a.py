import json
import random
import requests
import string


def send_req():
    url = "https://api-v2.mlytics.co/mdns/v2/_internal/zone/"
    name = ''.join(random.sample((string.digits + string.ascii_lowercase), 4))
    domain = "fqdntest.com"

    payload = json.dumps({
        "org_id": "1001659593134",
        "zone": {
            "zone_id": "bed9c178-cfc0-44cd-b1e9-daacbedca3dc",
            "domain": domain,
            "status": 1
        },
        "rrsets": [
            {
                "name": name + "." + domain,
                "type": "A",
                "ttl": 120,
                "proxied": False,
                "detail": [
                    {
                        "value": "1.1.1.1"
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
    for i in range(2):
        send_req()
        print(i)
