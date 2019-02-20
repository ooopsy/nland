import redis
import re

__ARTICAL__ = 'ARTICLE'
__PUSH_QUEUE__ = 'PUSH_QUEUE'
__USER_COMPLEX__ = 'USER_COMPLEX'
__USER__ = 'USER'



r=redis.Redis(host='127.0.0.1',port=6379)

def save_region(region):
    r.hmset('rpNo:' + region['rpNo']+':regionNo:' + region["cortarNo"], str(region))


def save_complex(complex):
    r.hmset("rNo:"+complex['cortarNo']+":complexNo:" + complex['complexNo'], str(complex))


def save_artical(artical):
    r.hset(__ARTICAL__, artical['key'], str(artical))


def drop_artical():
    keys =  r.hkeys(__ARTICAL__)

    for key in keys:
        r.hdel(__ARTICAL__, key.decode('utf-8'))

def drop_all():
    keys  = r.keys("*")

    for key in keys:
        r.delete(key.decode('utf-8'))


def exit_artical(artical):
    key = artical['key']
    return r.hexists(__ARTICAL__, key)

def save_push_articles(key):
    r.lpush(__PUSH_QUEUE__, key)

def get_article_detail(article_no):
    return r.hget(__ARTICAL__, article_no)


def get_push_article():
    return r.rpop(__PUSH_QUEUE__)

def add_user_pushlist(uno, ano):
    key = 'uno:{0}:pushlist'.format(uno)
    r.sadd(key, ano)

def add_user_complexes(uno, ano):
    key = 'cno:{0}:users'.format(uno)
    r.sadd(key, ano)


def get_user_pushlist(uno):
    key = 'uno:{0}:pushlist'.format(uno)
    return r.smembers(key)

def remove_user_pushlist(uno, ano):
    key = 'uno:{0}:pushlist'.format(uno)
    r.srem(key, ano)

def get_complex_user(cno):
    key = 'cno:{0}:users'.format(cno)
    return r.smembers(key)

def get_time_push_users(time):
    key  = 'time:{0}:users'.format(time)
    return r.smembers(key)

def add_time_push_users(time, user_no):
    key  = 'time:{0}:users'.format(time)
    return r.sadd(key, user_no)



def get_user_info(userno):
    return r.hget(__USER__, userno)


def save_user_info(user):
    r.hset(__USER__, user['user_no'], str(user))


def delete(key):
    r.delete(key)


if __name__ == '__main__':
    re =  r.rpop("queue")





