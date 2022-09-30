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
            "zone_id": "1b7e3a61-4cb4-4974-b90c-8eef88644194",
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

    if response.status_code == 200:
        print('Success!')
    elif response.status_code == 404:
        print('Not Found.')


if __name__ == '__main__':
    for i in range(1):
        send_req()
        print(i)
