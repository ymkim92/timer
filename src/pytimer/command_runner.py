"""command runner"""

import sys
from subprocess import STDOUT, check_output


def run_command(command, output_flag=True):
    """run command"""
    output = check_output(command, stderr=STDOUT, shell=True)
    if output_flag:
        print("$ " + command)
        sys.stdout.write(output.decode())


run_local_command = run_command
