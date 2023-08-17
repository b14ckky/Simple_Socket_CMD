import argparse
import socket
import json
import random
import sys

from termcolor import colored

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


if args.port and args.ip:
    host = args.ip
    port = args.port

s = socket.socket()


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


s.bind((host, port))
s.listen(2)
conn, addr = s.accept()
while True:
    cmd = input("\033[91m"+"cmd>"+"\033[0m")
    easy_send(conn, cmd)
    result = easy_recv(conn)
    print(result)

conn.close()
s.close()
