
Hàm `main()` </br>
![image](https://user-images.githubusercontent.com/23306492/39137756-8e679bd6-4748-11e8-9957-326921aec11e.png)</br> đọc source thì t thấy lỗi `format string`. Ở đây  khi `printf` xong thì `exit` với hàm `myspecialexitfunction()`</br>
![image](https://user-images.githubusercontent.com/23306492/39137847-ca8fcef8-4748-11e8-9bac-94a5422bc02f.png)</br> như vậy thì méo nào khai thác được. Yêu cầu t cần phải ghi đè địa chỉ của hàm `myinvisiblebackdoor()` </br>
![image](https://user-images.githubusercontent.com/23306492/39137923-fe27d814-4748-11e8-9762-c8387ca196a5.png)</br> mà méo biết ghi vào đâu. Ta thấy chương trình có sử dụng `alarm(0xAu)` cho nó in thật nhiều ra => nó sẽ bị quá giờ alarm, mà alarm gọi puts => ta ghi đè địa chỉ hàm `myinvisiblebackdoor()` vào `puts_got`</br>
![image](https://user-images.githubusercontent.com/23306492/39138420-143d4534-474a-11e8-8676-3f60163ba09a.png)</br>[payload.py](https://github.com/k4k4/MATESCTF_SESSION4/blob/master/echo/echo.py)
</br>
![image](https://user-images.githubusercontent.com/23306492/39138483-34fd8e8c-474a-11e8-9354-04013faa4f91.png)
