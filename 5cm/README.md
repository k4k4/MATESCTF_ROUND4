
Chương trình chính</br>
![image](https://user-images.githubusercontent.com/23306492/39137038-d58d0106-4746-11e8-921f-3b43e5906409.png)</br>
![image](https://user-images.githubusercontent.com/23306492/39137404-a85cb69e-4747-11e8-8324-bb2f16fb5e18.png)
</br>chương trình sẽ gọi `shellcode 5 byte` ta nhập vào </br>Ta cần viết shellcode cho phép nhập với `len` lớn hơn. Tham khảo  `https://defuse.ca/online-x86-assembler.htm` và `http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/` để viết shell </br>
![image](https://user-images.githubusercontent.com/23306492/39137284-6ac82a0c-4747-11e8-8c3c-0b5a69cd68f7.png)</br>
![image](https://user-images.githubusercontent.com/23306492/39137444-c3bfac52-4747-11e8-9a7e-44fc53c12067.png)</br>với `rdx = size_t count` thì ta tha hồ  mà nhập shellcode </br>[payload.py](https://github.com/k4k4/MATESCTF_SESSION4/blob/master/5cm/5cm.py)
</br>
![image](https://user-images.githubusercontent.com/23306492/39137537-0cb86052-4748-11e8-8031-c4b671ee984d.png)
