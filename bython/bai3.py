"""
video 7
KIỂU DỮ LIỆU Cơ BẢN TRONG BYTHON
  Các kiểu dữ liệu cơ bản:
   int: số nguyên.  VD: x=1
   float: số thực.  VD: x=2.3
   complex: số phức.  VD: x=1+2j
   bool: True/False.  VD: x= true  or x=false
   str: chuỗi ký tự.  VD: x='abd'
   NoneType: dối tượng đặc biệt cỉ ra giá trị NULL.  VD: X=None 
  -->không nhất thiết phải khai báo như trong C/C++
  kiểm tra kiểu dữ liệu của biến trong bython
   - lệnh kiểm tra: 
       print (type(x))

"""
x=1
print(type(x))
x=3.24
print(type(x))
x=1+2j
print(type(x))
x=True
print(type(x))
x=None
print(type(x))
"""
#kết quả:
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'bool'>
<class 'NoneType'>
"""

e = 2.72
pi = 3.14
text = "Xin chào Như Quỳnh"
print("kiểu dữ liệu của e: ",type(e), " kiểu dữ liệu của pi: ",type(pi), " kiểu dữ liệu của text: ",type(text))
"""
kết quả:
kiểu dữ liệu của e:  <class 'float'>  kiểu dữ liệu của pi:  <class 'float'>  kiểu dữ liệu của text:  <class 'str'>
"""

"""
video 8
ÉP KIỂU DỮ LIỆU (CHUYỂN DỔI KIỂU DỮ LIỆU)
- CHUYỂN ĐỔI KIỂU NGẦM ĐỊNH
   
"""
a=5
b=2.0
c=a/b
print(c)
print("kiểu dữ liệu của a:", type(a))
print("kiểu dữ liệu của b:", type(b))
print("kiểu dữ liệu của c:", type(c))

n=100
m="200"
print(str(n) + m)  #kết quả: 100200
print(n+int(m))   #kết quả: 300