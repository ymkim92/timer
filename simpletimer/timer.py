#!/usr/bin/env python3
# codeing=utf-8

import argparse

from subprocess import check_output, STDOUT
import sys
import time

def run_command(command, output_flag=True):
    output = check_output(command, stderr=STDOUT, shell=True)
    if output_flag:
        print("$ " + command)
        sys.stdout.write(output.decode())

run_local_command = run_command

class Timer:
    def __init__(self, minutes=30):
        self.minutes = minutes

    def start(self):
        self.start_time = time.time()
        print(time.asctime(time.localtime(self.start_time)))

    def get_time_diff(self):
        return time.time() - self.start_time

    def get_time_diff_string(self):
        diff_sec = time.time() - self.start_time
        return self.__format_time(diff_sec)

    def get_time_remaining_string(self):
        remaining_sec = (self.start_time + self.minutes*60) - time.time() 
        return self.__format_time(remaining_sec)

    def __format_time(self, sec):
        mint = int(sec / 60)
        sec = int(sec) % 60
        return '{}:{}'.format(mint, sec)

    def is_time_off(self):
        return time.time() > self.start_time + self.minutes * 60

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('minutes', type=int)
    return parser.parse_args(sys.argv[1:])

def pytimer():
    last_remained_time = ''

    args = get_arguments()

    timer = Timer(args.minutes)
    timer.start()
    try:
        while timer.is_time_off() == False:
            last_remained_time = timer.get_time_remaining_string()
            print(last_remained_time + '  ', end='\r', flush=True)
            time.sleep(1)

        print(time.asctime(time.localtime(time.time())))
        snd_complete = '/usr/share/sounds/freedesktop/stereo/complete.oga'
        command = "mplayer {}".format(snd_complete)
        run_local_command(command, False)
        command = "notify-send '{} minutes passed'".format(args.minutes)
        run_local_command(command)
    except KeyboardInterrupt:
        print("{}\nTimer stopped".format(last_remained_time))

# if __name__ == "__main__":
#     pytimer()