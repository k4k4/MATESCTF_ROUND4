Đề cho file nặng vãi mở ida lâu lét. mở lên t thấy chương trình có 99999 hàm `castle`. Mở vài cái `castle` thì thấy giống nhau t đoán chắc có 1 hàm `castle` nào đó sẽ `stack overflow`  </br>
![image](https://user-images.githubusercontent.com/23306492/39139114-4c9a1eec-474b-11e8-9735-6d04c19d7f5e.png)</br>Không biết có đúng không nhưng mà nó tìm vẫn dc cái địa chỉ hàm cần tìm `castle42590()` </br>
```
#objdump -d explorer |grep '$0x8,%edx' > a.txt
f = open('a.txt','r')
l = f.read().split("\n")

for i in range(len(l)-2):
	d = int('0x'+l[i+1][0:6],16) - int('0x'+l[i][0:6],16)
	# 0x4007ca - 0x40079f = 43 and 0x400800 - 0x4007ca=54
	if (d != 43) and (d != 54):
		print '0x'+l[i][0:6]
```
</br>
Hàm `Castle42590()` </br>

![image](https://user-images.githubusercontent.com/23306492/39140256-345756ee-474e-11e8-9f24-02c6655517fd.png)
</br>
![image](https://user-images.githubusercontent.com/23306492/39139697-c9e21926-474c-11e8-9470-9e99e82f0322.png)
</br> sử dụng `ret2libc` để exploit. Éo le cái là sao debug local đéo dc nhưng mà remote lên server lại dc [payload](https://github.com/k4k4/MATESCTF_SESSION4/blob/master/explorer/explorer.py)</br>
![image](https://user-images.githubusercontent.com/23306492/39139908-56d8b6dc-474d-11e8-9dc5-f332f921da97.png)


