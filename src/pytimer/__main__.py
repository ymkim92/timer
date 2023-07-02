"""main"""
import argparse
import sys
import time

from .command_runner import run_local_command
from .pytimer import Timer


def get_arguments():
    """get arguments"""
    parser = argparse.ArgumentParser()
    parser.add_argument("minutes", type=int)
    return parser.parse_args(sys.argv[1:])


def main():
    """main"""
    last_remained_time = ""

    args = get_arguments()

    timer = Timer(args.minutes)
    timer.start()
    try:
        while timer.is_time_expired() is False:
            last_remained_time = timer.get_time_remaining_string()
            print(f"{last_remained_time} ", end="\r", flush=True)
            time.sleep(1)

        print(time.asctime(time.localtime(time.time())))
        snd_complete = "/usr/share/sounds/freedesktop/stereo/complete.oga"
        command = "mplayer {}".format(snd_complete)
        run_local_command(command, False)
        command = "notify-send '{} minutes passed'".format(args.minutes)
        run_local_command(command)
    except KeyboardInterrupt:
        print("{}\nTimer stopped".format(last_remained_time))


if __name__ == "__main__":
    main()
