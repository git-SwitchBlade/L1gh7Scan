#!/usr/bin/env python3
import socket
import threading
from queue import Queue
import subprocess
import sys
import os


# color class
class color:
    blue = '\033[94m'
    green = '\033[92m'
    orange = '\033[93m'
    underline = '\033[4m'
    reset = '\033[0m'


# first banner
def banner():
    os.system('clear')
    print(f'{color.blue}----------------------------------------------------------')
    print(r"""
        __   ___      __ __________
       / /  <  /___ _/ //__  / ___/_________ _____
      / /   / / __ `/ __ \/ /\__ \/ ___/ __ `/ __ \
     / /___/ / /_/ / / / / /___/ / /__/ /_/ / / / /
    /_____/_/\__, /_/ /_/_//____/\___/\__,_/_/ /_/
            /____/
    """)
    print('----------------------------------------------------------')
    print('[+] You should have latest Version of NMAP installed')
    print('[+] Developed By $witch<Blade#0001')
    print(f'[+] Only supports IPv4{color.reset}')
    print(f'{color.orange}[+] I am not Rusted{color.orange}')
    print(f'{color.blue}----------------------------------------------------------\n\n{color.reset}')


# scanning ports
def portscan(port):
    # connecting to the remote host
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        con = s.connect((host, port)) # scanning the ports
        with print_lock:
            print(f'{color.green}[+] port {port} is open{color.reset}')
            open_ports.append(port)
        con.close()
    except BaseException:
        pass


def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


if __name__ == '__main__':
    banner()

open_ports = []
print_lock = threading.Lock()

if not sys.argv[1:]:
    print(f'{color.orange} [+] Invalid Usage')
    print(f'{color.orange} [+] Correct Usage `python3 Lightscan.py 127.0.0.1`')
    exit(1)
else:
    host = sys.argv[1]

q = Queue()


for x in range(700):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1, 65535):
    q.put(worker)


# nmap scan
q.join()
separator = ", "
apple = separator.join(map(str, open_ports))
print(f'{color.blue}\n \n ----------------------------------------------------------')
print('[+] All the ports are Scanned')
print(f'[+] Executing Nmap scan on the discovered ports, [nmap {host} -vvv -T4 -p {apple}]')
print(f'----------------------------------------------------------{color.reset}')
print(color.green)
output = subprocess.check_output(['nmap', host, '-T4', '-p', apple])
print(output.decode('utf-8'))
print(color.reset)
