import socket
import threading
from queue import Queue
import subprocess

print('----------------------------------------------------------')
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
print('[+] Only supports IPv4')
print('----------------------------------------------------------\n\n')
open_ports = []
print_lock = threading.Lock()
host = input("Enter Host IP:")

def portscan(port):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(0.5)
	try:
		con = s.connect((host, port))
		with print_lock:
			print('[+] port', port, 'is open')
			open_ports.append(port)
		con.close()
	except:
		pass

def threader():
	while True:
		worker = q.get()
		portscan(worker)
		q.task_done()

q = Queue()

for x in range(700):
	t = threading.Thread(target = threader)
	t.daemon = True
	t.start()

for worker in range(1, 65535):
	q.put(worker)

q.join()
print('\n \n ----------------------------------------------------------')
print('[+] Now All the ports are Scanned')
print('[+] Our Nmap Come in Action, [nmap host -sCV -T4 -p open_ports]')
print('----------------------------------------------------------')
separator = ", "
apple = separator.join(map(str, open_ports))
output = subprocess.check_output(['nmap', host, '-vvv', '-T4', '-p', apple])
print(output.decode('utf-8'))