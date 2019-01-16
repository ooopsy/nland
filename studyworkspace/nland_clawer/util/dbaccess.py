import redis
import re


r=redis.Redis(host='127.0.0.1',port=6379)

def save_region(region):
    r.hmset('rpNo:' + region['rpNo']+':regionNo:' + region["cortarNo"], region)


def save_complex(complex):
    r.hmset("rNo:"+complex['cortarNo']+":complexNo:" + complex['complexNo'], complex)


def save_artical(artical):
    r.hmset(artical['key'], artical)

def artical_count(artical):
    key = artical['key']
    return len(r.keys(key))



