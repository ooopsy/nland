from __future__ import print_function

import os
import sys
import time
import json
import requests
import argparse
import lxml.html
import io
from util import my_http
from util import dbaccess

from lxml.cssselect import CSSSelector

NEW_NAVER_LAND_URL = 'https://new.land.naver.com/api/articles/complex/{0}?tradeType=A1&page={1}'


def artical(complex_no, pageno):
    res = my_http.send_request(NEW_NAVER_LAND_URL.format(complex_no));

    for ar in res:
        ar['complexNo'] = complex_no
        dbaccess.save_artical(ar)

    if res['isMoreData'] :
        artical(complex_no, pageno +1)





