from datetime import datetime, timedelta
from time import sleep


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Timer(metaclass=Singleton):
    _timestamp = None

    def __init__(self, freeze_time_sec: int = 1):
        self._freeze_time = timedelta(seconds=freeze_time_sec)

    def background_pause(self):
        if self._timestamp is None:
            self._timestamp = datetime.now()
            return True

        delta = (datetime.now() - self._timestamp)
        if delta > self._freeze_time:
            return True
        else:
            wait_time_delta = self._freeze_time - delta
            wait_time = wait_time_delta.seconds * 1000 + wait_time_delta.microseconds / 1000000.0
            sleep(wait_time)
            self._timestamp = datetime.now()
            return True


timer = Timer(5)
