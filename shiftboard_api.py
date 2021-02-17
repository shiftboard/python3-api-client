#!/usr/bin/python3

# API Documentation: https://www.shiftdata.com

import base64
import hashlib
import hmac
import json
import urllib.parse
import urllib.request

API_URL = 'https://api.shiftdata.com'
signature_key = 'YOUR SIGNATURE KEY'
access_key_id = 'YOUR API ACCESS KEY'

method = 'system.echo'

params = {
  'foo': 'bar',
  'answer': 42,
  'dinner': 'nachos'
}

params_string = json.dumps(params, separators=(',', ':'))
params_base64 = base64.urlsafe_b64encode(params_string.encode())

signature_data = 'method' + method + 'params' + params_string
signature = base64.urlsafe_b64encode(hmac.HMAC(signature_key.encode(), signature_data.encode(), hashlib.sha1).digest())

url = API_URL + '?' + urllib.parse.urlencode({
    'id': 1,
    'jsonrpc': '2.0',
    'method': method,
    'params': params_base64,
    'access_key_id': access_key_id,
    'signature': signature
})

httpresponse = urllib.request.urlopen(url)
response = json.loads(httpresponse.read())
print(response)
