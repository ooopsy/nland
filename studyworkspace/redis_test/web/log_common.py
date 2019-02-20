import time
from datetime import datetime


def logcommon(conn, name, message, serviry = 'INFO', timeout=5):
    severity = 'INFO'
    destination = 'common%s.%s'%(name, serviry)
    start_key = destination + ':start'
    pipe = conn.pipeline()
    end = time.time() + timeout

    while time.time() < end:
        try:
            pipe.watch(start_key)
            now  = datetime.utcnow().timetuple()
            hour_start = datetime(*now[:4]).isoformat()
            existing = pipe.get(start_key)
            pipe.multi()
            if existing and existing < hour_start:
                pipe.rename(destination, destination + ':last')
                pipe.rename(start_key, destination + ':pstart')
                pipe.set(start_key, hour_start)

            pipe.zincrby(destination, message)
            #log_recent(pipe, name, message, severity, pipe)
            return None;

        except EnvironmentError:
            continue