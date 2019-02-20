import time
import datetime

SEVERITY = {
    'DEBUG': 'debug',
    'INFO' : 'info',
    'WARNING': 'warning',
    'ERROR': 'error',
    'CRITICAL': 'critical'
}

SEVERITY.update((name, name) for name in SEVERITY.values())

def log_recent(conn, name, message, severity='INFO', pipe=None):
    severity = str(SEVERITY.get(severity, severity)).lower()
    destination = 'recent:%s:%s'%(name, severity)
    message = time.asctime() + '' + message
    pipe = pipe or conn.pipeline()
    pipe.lpush(destination, message)
    pipe.ltrim(destination, 0, 99)
    pipe.execute()

