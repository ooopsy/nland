import redis
import time
import threading


conn=redis.Redis(host='127.0.0.1',port=6379)


def publisher(n):
    time.sleep(1)
    for i in range(n):
        conn.publish('channel', i)
        time.sleep(1)

# 当没有 sub 的channel时主线程结束 反之一直处在监听状态
def run_pubsub():
    threading.Thread(target=publisher, args=(3,)).start()
    pubsub = conn.pubsub()
    pubsub.subscribe(['channel'])
    count = 0
    for item in pubsub.listen():
        print(item)
        count +=1
        if count == 4:
            pubsub.unsubscribe()
        if count == 5:
            break


run_pubsub()
