import redis
import time


QUIT = False
LIMIT = 10

r=redis.Redis(host='127.0.0.1',port=6379)


def clean_session():
    while not QUIT:
        print("exec clean_session")
        size = r.zcard("recent:")
        if size <= LIMIT:
            time.sleep(1)
            continue


        end_index = min(size - LIMIT, 100)
        tokens = r.zrange("recent:", 0, end_index - 1)
        session_keys =  ['views:' + token for token in tokens]

        r.delete(*session_keys)
        r.hdel("login:", *tokens)
        r.zrem("recent:", *tokens)



if __name__ == "__main__":
    clean_session()