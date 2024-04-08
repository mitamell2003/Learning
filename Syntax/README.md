# Dùng để chạy Python 
- gõ lệnh `python` ở đầu + Tên file mình muốn chạy
```
python '.\Hello world\hello_world.py'

--->hi
```
---
# Thụt lề Python
- Mỗi câu điều kiện if phải có câu lệnh được quy định bằng khoảng cách thụt dòng vào, nếu không thụt dòng thì sẽ được xem là cùng cấp với if không chạy được.
- Lưu ý: Mỗi điều kiện có thể có nhiều câu lệnh nhưng bên trong câu lệnh không thể có câu lệnh.
```py
if 5 > 2:
    print("năm lớn hơn hai!")
# đúng
if 5 > 2:
print("năm lớn hơn hai!")
# or
if 5 > 2:
    print("năm lớn hơn hai!")
        print("năm lớn hơn hai!")
# sai
```
# Biến (variables) Python
- Gán giá trị X, Y cho các biến, sau đó in các giá trị ra màn hình
```py
X = 13
Y = "Gioi"
print(X)
print(Y)
```
# Thay đổi giá trị ban đầu
- Với giá trị được thiết lập ban đầu có thể thay đổi được và không cần phải khai báo với một theo một kiểu cụ thể nào.
```py
X = 5
X = "NĂM"
print(X)
```
# Quy định kiểu dữ liệu 
- có thể quy định kiểu dữ liệu được in ra theo mong muốn qua các hàm như: `str`, `int`, `float`
```py
X = str(3)
Y = int(3)
Z = float(3)
print(X)
print(Y)
print(Z)
```
# Lấy kiểu dữ liệu với hàm. `type()`
- Có thể lấy kiểu dữ liệu của một biến bằng cách dùng hàm. `Type()`
```PY
X = 5
Y = 'hello'
Z = 3.5
print(type(X))
print(type(Y))
print(type(Z))
```
# Biến chuỗi có thể được khai báo bằng cách sử dụng dấu ngoặc kép hoặc dấu ngoặc kép
```PY
X = "HI"
# Same as
X = 'HI'
```
# Tên biến có thể phân biệt giữa chữ hoa và thường
```py
a = 5
A = "Hello"
```
# Quy tắc đặt tên biến
- Tên biến phải bắt đầu bằng chữ cái hoặc dấu gạch dưới.
- Tên biến `không thể` bắt đầu bằng một số.
- Tên biến `chỉ có thể`chứa các chữ cái, số và dấu gạch dưới.
- Tên biến phân biệt giữa chữ hoa và chữ thường (tuổi, Tuổi, TUỔI là ba biến khác nhau).
- Tên biến không thể chứa các từ khóa của Python.