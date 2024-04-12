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
```py
Name = 'mini'
Name_Cat = "mini"
_Name = "mini"
Name_01 = 'mini'
name = "cat"
# True
01 = 'mini'
and = "mini"
Name cat = "mini"
# False
```
# Gán giá trị cho nhiều biến
- có thể gán nhiều giá trị cho một biến trong một dòng.
```py
X, Y, Z = "Chó", "Mèo", "Chuột"
print(X)
print(Y)
print(Z)
```
# Gán một giá trị cho nhiều biến
```py
X = Y = Z = "Mây"
print(X)
print(Y)
print(Z)
```
# Giải nén
- khi có một tập hợp các giá trị có thể trích xuất thành các biến
```py
Trái_Cây = ["Cam", "Mận", "Xoài"]
X, Y, Z = Trái_Cây
print(X)
print(Y)
print(Z)
```
# Hàm `print()`
- Có thể viết liền các biến với nhau bằng dấu `+` hoặc `,`
- Lưu ý: Dấu `+` chỉ dùng khi các biến có cùng kiểu dữ liệu với nhau
```py
X, Y, Z = 'Tên', 'Tui', 'là'
print(X + Y + Z)
print(X, Y, Z)
# or
X, Y, Z = 'Tuổi', 15, 10
print(X, Y, Z)
# True
X, Y, Z = 'Tuổi', 15, 10
print(X + Z)
# False
```
# Biến toàn cục
- `Biến toàn cục` được tạo bên ngoài một hàm, có thể sử dụng lại được nhiều lần.
```py
X = 'Tiên'
def tentien():
    print('Tên là ' + X)
tentien()    
```
- Có thể tạo một biến (cùng tên với biến toàn cục) bên trong hàm được gọi là `biến cục bộ` và chỉ sử dụng bên trong hàm đó, Không ảnh hưởng đến biến toàn cục
```py
X = 'Cat'
def animal():
    X = 'Động vật ăn thịt'
    print('Mèo là ' + X)
animal()
print(X + 'is an animal')
```
# Tạo biến toàn cục bên trong hàm
- Có thể tạo biến toàn cục bên trong hàm thay vì chỉ tạo được biến cục bộ bằng cách dùng lện `global`
```py
x = 'Apple'
def name():
    global X
    X = 'Banana'
name()
Print('Chuối' + X)
```
# Kiểu dữ liệu
- Python có các kiểu dữ liệu sau được tích hợp sẵn theo mặc định, trong các danh mục sau:
```py

Text_Type:	str
Numeric_Types:	int, float, complex
Sequence_Types:	list, tuple, range
Mapping_Type:	dict
Set_Types:	set, frozenset
Boolean_Type:	bool
Binary_Types:	bytes, bytearray, memoryview
None_Type:	NoneType
```
# Type()
- Có thể lấy kiểu dữ liệu bằng cách sử dụng hàm `Type()`
```py
X = 5
Print(Type(X))
```
# Python number
- Trong python có 3 loại số:
+ `int`
+ `float`
+ `complex`
- có thể chuyển đổi kiểu này sang kiểu khác 
```py
X = 2 #int
Y = 2.0 #float
Z = 3j #complex
a = float(X)
b = int(Y)
c = complex(Z)
print(a)
print(b)
print(c)
```
- Lưu ý: Không thể chuyển đổi kiểu `complex`sang các kiểu khác
# Random
- Python không thể tạo các số ngẫu nhiên nhưng có thể dùng modum tích hợp `Random()`
```py
import random
print(random.randrange(1, 10))
```
# Chỉ định loại biến
- có thể chỉ định loại biến `int`, `float`, `str`
- `int` chứa các số nguyên 
- `float` chứa các số thập phân
- `str` chứa các chuỗi, số nguyên và số thập phân 
```py
X = int(2)
Y = int(3.9)
Z = int("2")
a = float(2.0)
b = float(3)
c = float('4')
x = str('s1')
y = str(3)
z = str(3.0)
print(X, Y, Z, a, b, c, x, y, z)
```