import json
from datetime import datetime

def event2json(event) -> dict:
    return json.loads(str(event))

def datetime_now() -> datetime:
    return datetime.now()

def timestamp_converter(timestamp) -> str(datetime):
    """[summary]
    Args:
        timestamp ([int]): 
            input timestamp is milliseconds
            get rid of it and transger to string datetime
    """
    timestamp: int =int(str(timestamp)[:-3])
    str_datetime: str = datetime.strftime(datetime.fromtimestamp(timestamp), "%Y-%m-%dT%H:%M:%S")
    return str_datetime

def logs_handler(logs):
    """[summary]

    Args:
        message types:
            text, sticker, audio, location, image, video
            
    """
    logs = event2json(logs)['events'][0]
    print(logs)
