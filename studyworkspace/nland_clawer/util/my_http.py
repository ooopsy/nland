#!/usr/bin/python
# -*- coding: UTF-8 -*-


import requests
import json

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

def send_request(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    response = session.get(url)
    return json.loads(response.text)