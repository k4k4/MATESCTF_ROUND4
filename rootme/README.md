Hàm` main`</br>![image](https://user-images.githubusercontent.com/23306492/39135457-2edc1fe8-4743-11e8-8f27-dbdb67e54841.png)</br>function `regroot` tạo account root trong heap </br>
![image](https://user-images.githubusercontent.com/23306492/39135664-a753f086-4743-11e8-8686-3da51f9acd6a.png)</br>`getflag` khi `mode != 0`</br>
![image](https://user-images.githubusercontent.com/23306492/39135731-d29effd8-4743-11e8-8f3f-fcaf9b6cb63e.png)</br> 
![image](https://user-images.githubusercontent.com/23306492/39135965-6225fbfc-4744-11e8-9c73-e2f973b756b1.png)</br>
để `mode = 1` thì cần login với tài khoản `root`  </br>ta xác định password root có 29 ký tự </br>
![image](https://user-images.githubusercontent.com/23306492/39136063-9e38c0e8-4744-11e8-919b-2f6ecaa7fe52.png)</br>
hàm `reg`</br>
![image](https://user-images.githubusercontent.com/23306492/39136107-b18014f8-4744-11e8-9b90-6d2be3332ab4.png)</br>hàm `del` </br>
![image](https://user-images.githubusercontent.com/23306492/39136131-bf05918e-4744-11e8-90ea-cf77e7b3caf5.png)</br> lỗi ở đây là ta có thể `brute force  password root`  với 29 lần connect lên server mỗi lần ta có thể biết đc 1 ký tự [solution](https://github.com/k4k4/MATESCTF_SESSION4/blob/master/rootme/rootme.py)</br>
![image](https://user-images.githubusercontent.com/23306492/39136359-3cb86bb0-4745-11e8-8d27-c6132dacddd4.png)
