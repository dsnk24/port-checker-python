import queue
import socket
import threading
import sys
from queue import Queue

target = "127.0.0.1"

queue = Queue()

if len(sys.argv) != 1:
    target = sys.argv[1]
else: pass

open_ports = []

def portscan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        sock.connect((target, port))

        return True
    
    except:
        return False


def fill_queue(port_list):
    for port in port_list:
        queue.put(port)


def worker():
    while not queue.empty():
        port = queue.get()

        if portscan(port):
            print(f'Port {port} is open!')
            open_ports.append(port)


port_list = range(1, 10000)

fill_queue(port_list=port_list)

thread_list = []

for t in range(20):
    thread = threading.Thread(target=worker)
    thread_list.append(thread)

for thread in thread_list:
    thread.start()

for thread in thread_list:
    thread.join()

print(f"Open ports: {open_ports}")