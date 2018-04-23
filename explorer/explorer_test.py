#objdump -d explorer |grep '$0x8,%edx' > a.txt
f = open('a.txt','r')
l = f.read().split("\n")

for i in range(len(l)-2):
	d = int('0x'+l[i+1][0:6],16) - int('0x'+l[i][0:6],16)# 0x4007ca - 0x40079f = 43 and 0x400800 - 0x4007ca=54
	if (d != 43) and (d != 54):
		print '0x'+l[i][0:6]
		