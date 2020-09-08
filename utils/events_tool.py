import json
import time

def event2json(event) -> dict:
    return json.loads(str(event))

def timestamp2date(timestamp) -> time:
    
    return time.ctime(timestamp)