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
# Chuỗi nhiều dòng
- có thể gán một chuỗi nhiều dòng bằng cách sử dụng `"""` hoặc `'''`
```py
a = ''' Nguyễn Văn A,
1012/1111/111,
địa chỉ: zzzzzz,zzzzzzz '''
print(a)  
```
# Chuỗi là một mảng
- Python không có kiểu dữ liệu ký tự, một ký tự đơn giản là một chuỗi có độ dài là 1 
- Có thể sử dụng dấu `[]` để truy cập tới các phần tử của chuỗi
```py
X = 'Nguyễn A'
print(X[3])
```
# For loop string
```py
for X in 'Mini':
    print(X)
```
# Độ dài chuỗi
- Có thể đo độ dài một chuỗi `len()`
```py
X = 'Nguyễn A'
print(len(X))
```
# kiểm tra một từ hay một cụm từ có hay không có trong chuỗi 
- để kiểm tra một từ hay một cụm từ có trong chuỗi sử dụng từ `in`
```py
Text = 'Thằng giới đáng ghét'
print('ghét' in Text)
```
- hoặc thêm `if`
```py
Text = 'Thằng giới đáng ghét'
if 'ghét' in Text:
    print('Có ở trong đây nha má !')
```
- Ngược lại khi không có thì chỉ cần thêm dùng `not in`
```py
Text = 'Thằng giới đáng ghét'
if 'thương' not in Text:
    print('không có ở trong đây nha má !')
```
# Slicing
```py
X = 'Đinh Thị Thu Nguyên'
print(X[2:5])
```
- Bắt đầu từ số 0, và sẽ lấy từ 2 đến 4
# Slice From the Start and the end
```py
X = 'Mini, mèo'
print(X[:4])
```
- Khi đặt dấu `:` ở trước số ký tự muốn lấy thì sẽ được hiểu là lấy từ đầu đến số đó và ngược lại cho phần end
```py
X = 'Mini, mèo'
print(X[4:])
```
# Negative Indexing
- có thể chỉ định bằng số âm bằng cách điếm từ cuối lên 
```py
fruits = 'banana, apple'
print(fruits[-4:-1])
```
- lưu ý : Số phía trước phải nhỏ hơn số phía sau và chỉ có thể cùng là số nguyên âm hoặc cùng là số nguyên dương 
# Viết Hoa `upper()`
```py
A = 'chó giới'
print(A.upper())
```
# Viết Thường `lower()`
```py
A = 'Chó Gioi'
print(A.lower())
```
# Loại bỏ khoảng trắng
```py
b = " hi, my name is bò / " 
print(b.strip())
```
# Thay thế chuỗi
```py
b = "hi, my name is bò" 
print(b.replace("h", "L")) 
```
# Tách Chuỗi
```py
b = " hi, my name is bò  " 
print(b.split(","))
```
# Nối Chuỗi 
- Có thể nối chuỗi bằng dấu `+` và thêm khoảng trắng ở giữa các chuỗi cần nối bằng dấu `" "`
# String format
- Có thể nối các chuỗi không cùng kiểu với nhau thông qua f-String `f {}`
```py
X = 38
text = f"ông Lâm năm nay {X} tuổi"
print(text)
```
- Có thể sữa đổi kiểu từ số nguyên sang số thập phân thông qua `:.2f`
```py
X = 87
text = f"Số {X:.2f} là số thập phân"
print(text)
```
- Thực hiện các phép toán
```py
text = f"đáp án của phép toán trên là {20*56}"
print(text)
```
# Escape Characters
- `\'`	(dấu ')	
- `\\`	(dấu \ )	
- `\n`	(dòng mới)	
- `\r`	(chuyển lên đầu)	
- `\t`	(Tab)	
- `\b`	(Backspace)	
- `\f`	(dữ liệu mẫu)	
- `\ooo`(Octal value)	
- `\xhh`(Hex value)
# Bool
- Bool sẽ trả về giá trị `True`, `False` .Đa số sẽ là `True` trừ một số trường hợp sau:`0`, `False`, `None`, và khoảng trắng
# Toán tử
- Python chia các toán tử thành các nhóm sau:
+ Toán tử số học
+ Toán tử gán
+ Toán tử so sánh
+ Toán tử logic
+ Toán tử danh tính
+ Nhà điều hành thành viên
+ Toán tử Bitwise
# List
- có thể in ra một thành phần hoặc một khoảng trong danh sách
- Có thể thay đổi một hay một phạm vi trong danh sách
```py
list = ['cây', 'chó', 'mèo']
list[1] = 'Mít'
print(list)
```
- có thể thêm một thành phần mới vào danh sách bằng cú pháp `append()` sẽ tự động chèn vào cuối danh sách hoặc `insert()` để thêm vào vị trí mong muốn 
```py
list = ['táo', 'cam', 'xoài', 'ổi']
list.append('quýt')
print(list)
```
```py
list = ['táo', 'cam', 'xoài', 'ổi']
list.insert(2, 'quýt')
print(list)
```
- có thể xóa bằng cú pháp `remove()` 
```py
list = ['cúc', 'đào', 'ớt']
list.remove('đào')
print(list)
```
- Khi danh sách có nhiều tên trùng với nhau thì `remove()` sẽ xóa item đứng trước
```py
list = ['mít', 'cam', 'xoài', 'mận', 'mít']
list.remove('mít')
print(list)
```
- xóa mục bằng cú pháp `pop()`, khi không điền thứ tự của item thì sẽ tự động xóa item cuối cùng
```py
list = ['cafe', 'trà', 'nước', 'đá']
list.pop(1)
print(list)
```
```py
list = ['cafe', 'trà', 'nước', 'đá']
list.pop()
print(list)
```
- Cũng có  thể xóa bằng key `del()`
```py
list = ['cafe', 'trà', 'nước', 'đá']
del list[0]
print(list)
```
- Xóa toàn bộ danh sách, sẽ xóa luôn danh sách này
```py
list = ['cafe', 'trà', 'nước', 'đá']
del list()
print(list)
```
- làm trống danh sách `clear()`. Danh sách vẫn còn, nhưng nó không có nội dung.
```py
list = ['cafe', 'trà', 'nước', 'đá']
list.clear()
print(list)
```
- có thể mở rộng danh sách, kết hợp các danh sách bằng lệnh `extend()`
```py
list = ['cafe', 'trà', 'nước', 'đá']
Mylist = ['cúc', 'đào', 'ớt']
list.extend(Mylist)
print(list)
```
# Vòng lập `for`
```py
list = ['mango', 'banana', 'apple']
for x in list:
    print(x)
```
# Loop list
```py
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
```
- `while`
```py
Tam = ['ta','Ta','tA']
i = 0
while i < len(Tam):
    print(Tam[i])
    i = i + 1
```
- Viết tắt
```py
myname = ['a','b','c']
[print(x) for x in myname]
```
# List Comprehension
```py
animal = ['duck', 'chicken', 'dog', 'fish', 'cobra', 'cat']
newlist = []
for x in animal:
    if 'c' in x:
        newlist.append(x)
print(newlist)
```
- viết tắt
```py
animal = ['duck', 'chicken', 'dog', 'fish', 'cobra', 'cat']
newlist = [x for x in animal if 'c' in x]
print(newlist)
```
# Sắp xếp `sort()`
- `sort()` sẽ mặc định sắp xếp theo thứ tự tăng dần 
```py
animal = ['duck', 'chicken', 'dog', 'fish', 'cobra', 'cat']
animal.sort()
print(animal)
```
- để sắp xếp theo thứ tự giảm dần thì dùng thêm từ khóa `reverse = true`
```py
number = [100, 10, 4, 15, 120, 1]
number.sort(reverse = True)
print(number)
```
- có thể tùy chỉnh chức năng sắp xếp thông qua từ khóa `key = function`
```py
def myfunc(n):
    return abs(n - 50)
number = [100, 10, 4, 15, 120, 1]
number.sort(key = myfunc)
print(number)
```
- `sort()` sẽ tự động sắp xếp các chữ cái viết hoa trước các chữ cái viết thường,
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
animal.sort()
print(animal)
```
- vì vậy nếu không muốn có sự phân biệt giữ chữ viết hoa và thường thì có thể sử dụng từ khóa `key = str.lower`
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
animal.sort(key = str.lower)
print(animal)
```
- có thể đảo ngược danh sách thông qua `reverse()`
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
animal.reverse()
print(animal)
```
# Syntax
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
newlist = [x for x in animal if x !='duck']
print(newlist)
```
```py
newlist = [x for x in range(10) if x < 3]
print(newlist)
```
- có thể đặt kết quả tùy nhu cầu
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
newlist = [x.upper() for x in animal if x != "Dog"] 
print(newlist)
```
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
newlist = [x if x != 'Chicken' else 'crab' for x in aniaml]
print(newlist)
```
# coppy list
- Bạn không thể sao chép một danh sách đơn giản bằng cách gõ , bởi vì: `list2 = list1 list2 list1 list1 list2` sẽ chỉ là một tham chiếu đến
- có thể sử dụng `copy()` và `list()` để tạo ra một bản sao
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
newlist = animal.copy()
print(newlist)
```
```py
animal = ['duck', 'Chicken', 'Dog', 'fish', 'Cobra', 'cat']
newlist = list(animal)
print(newlist)
```
# join list 
- có thể kết hợp hai danh sách bằng dấu `+`, `append()`, `extend()`
```py
list1 = [1, 3, 5, 7]
list2 = ['a','b','c','d']
newlist = list1 + list2
print(newlist)
```
```py
list1 = [1, 3, 5, 7]
list2 = ['a','b','c','d']
for x in list2
    list1.append(x)
print(x)
```
```py
list1 = [1, 3, 5, 7]
list2 = ['a','b','c','d']
list1.extend(list2)
print(list1)
```

