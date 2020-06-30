import http.client
import urllib.parse
import json
import ssl 

def send_messege_to_slack():
    params = urllib.parse.urlencode({'payload' : json.dumps({"text": "It's time to go home! Thanks for your hard work!"})})
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    context = ssl._create_unverified_context()
#    conn = http.client.HTTPConnection('hooks.slack.com')
    conn = http.client.HTTPSConnection('hooks.slack.com', context=context)
    conn.request(
        'POST',
        '/services/T0KFH5M6U/B4D66M7UM/bHt9AtpYbxiw9gqAeQSVd9Rp',
        params,
        headers)

    response = conn.getresponse()
    print(response.status, response.reason, response.msg)
    conn.close()

send_messege_to_slack()
