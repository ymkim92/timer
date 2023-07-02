"""pytimer"""

import time


class Timer:
    """timer class"""

    def __init__(self, minutes=30):
        self.minutes = minutes
        self.start_time = None

    def start(self):
        """start"""
        self.start_time = time.time()
        print(time.asctime(time.localtime(self.start_time)))

    def get_time_diff(self):
        """get time diff"""
        return time.time() - self.start_time

    def get_time_diff_string(self):
        """get time diff as string"""
        diff_sec = time.time() - self.start_time
        return self.__format_time(diff_sec)

    def get_time_remaining_string(self):
        """get remaining time as string"""
        remaining_sec = (self.start_time + self.minutes * 60) - time.time()
        return self.__format_time(remaining_sec)

    def __format_time(self, sec):
        mint = int(sec / 60)
        sec = int(sec) % 60
        return f"{mint}:{sec}"

    def is_time_expired(self):
        """is time expired"""
        return time.time() > self.start_time + self.minutes * 60
