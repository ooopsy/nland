import redis
import re

templace = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

r=redis.Redis(host='127.0.0.1',port=6379)


def save_region(region):
    r.hmset('rpNo:' + region['rpNo']+':regionNo:' + region["cortarNo"], region)


def save_complex(complex):
    r.hmset("rNo:"+complex['regionNo']+":complexNo:" + complex['complexNo'], complex)

def save_artical(artical):
    complexNo = artical['complexNo']


    r.hmset("complex:complexNo:" + complex['complexNo'] + "", complex)

