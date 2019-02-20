import redis
import time
import threading

conn=redis.Redis(host='127.0.0.1',port=6379)


def notrans():
    pipeline = conn.pipeline()
    print(pipeline.incr('trans:'))
    time.sleep(.1)
    pipeline.incr('trans:', -1)
    print(pipeline.execute()[0])

if 1:
    for i in range(3):
        threading.Thread(target=notrans).start()

    time.sleep(.5)
