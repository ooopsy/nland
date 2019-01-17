import redis
import re

__ARTICAL__ = 'ARTICLE'


r=redis.Redis(host='127.0.0.1',port=6379)

def save_region(region):
    r.hmset('rpNo:' + region['rpNo']+':regionNo:' + region["cortarNo"], region)


def save_complex(complex):
    r.hmset("rNo:"+complex['cortarNo']+":complexNo:" + complex['complexNo'], complex)


def save_artical(artical):
    r.hset(__ARTICAL__, artical['key'], artical)

def exit_artical(artical):
    key = artical['key']
    return r.hexists(__ARTICAL__, key)




if __name__ == '__main__':
    re =  r.hget(__ARTICAL__, 'cNo:10689:articalNo:1901381367:price:3억59,000')
    print(re)
