# /usr/bin/python3
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
    red = '\033[93m'
    underline = '\033[4m'
    reset = '\033[0m'



# first banner
def banner():
    os.system('clear')
    print(f'{color.blue}----------------------------------------------------------------')
    print(r"""
        __   ___      __ __________                
       / /  <  /___ _/ //__  / ___/_________ _____ 
      / /   / / __ `/ __ \/ /\__ \/ ___/ __ `/ __ \
     / /___/ / /_/ / / / / /___/ / /__/ /_/ / / / /
    /_____/_/\__, /_/ /_/_//____/\___/\__,_/_/ /_/ 
            /____/                                
    """)
    print('----------------------------------------------------------------')
    print('[+] You should have latest Version of NMAP installed')
    print('[+] Developed By $witch<Blade#0001')
    print(f'[+] Only supports IPv4{color.reset}')
    print(f'{color.red}[+] I am not Rusted{color.reset}')
    print(f'{color.blue}----------------------------------------------------------------\n\n{color.reset}')


# scanning ports
def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # connecting to the remote host
    s.settimeout(1)
    try:
        con = s.connect((host, port))        # scanning the ports
        with print_lock:
            print(f'{color.green}[+] port {port} is open{color.reset}')
            open_ports.append(port)
        con.close()            # closing connection
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()


# printing banner
if __name__== '__main__':
    banner()

open_ports = []        
print_lock = threading.Lock()
host = sys.argv[1]
try:
	protocol = sys.argv[2]  #User Specified Protocol
except IndexError:
	protocol = '-vvv' #Default Prtocol


q = Queue()


for x in range(700):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()

for worker in range(1, 65535):
    q.put(worker)


# nmap scan
q.join()
print(f'{color.blue}\n \n ----------------------------------------------------------')
print('[+] Now All the ports are Scanned')
print(f'[+] Our Nmap Come in Action, [nmap host {protocol} -T4 -p open_ports]')
print(f'----------------------------------------------------------{color.reset}')
separator = ", "
apple = separator.join(map(str, open_ports))
print(color.green)
output = subprocess.check_output(['nmap', host, protocol, '-T4', '-p', apple])
print(output.decode('utf-8'))
print(color.reset)
