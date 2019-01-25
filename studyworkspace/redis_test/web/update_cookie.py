import redis
import time
import random


r=redis.Redis(host='127.0.0.1',port=6379)




def update_cookie(token, user, item):
    now = time.time()

    r.hset("login:", token, user)
    r.zadd("recent:", token, now)

    if item:
        r.zadd("views:" + token, item, now)
        r.zremrangebyrank("views:" + token, 0, -26)



if __name__ == '__main__':
    for num in range(0, 50):
        sleep_time = random.randint(500, 2000)
        time.sleep(sleep_time / 1000)
        print(sleep_time / 1000)
        update_cookie('token880523', 'oopsy', 'p00'+ str(num)) ;














