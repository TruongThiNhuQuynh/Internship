"""
VIDEO 12
thư viện toán học "math" trong bython
- CÚ PHÁP: math.<tên hàm mà bạn cần>
  + math.ceil(x): số nguyên nhỏ nhất >= x (vd:nếu đưa vào 3.5 thì tre về 4)
  + math.floor(x): số nguyên lớn nhất <= x (vd:nếu đưa 3.5 thì trả về 3)
  + math.fabs(x): trả về giá trị tuyệ đối của x
  + math.exp(x): trả về e lũy thừa x (cơ số logarit tự nhiên)
  + math.log(x[,base]): với 1 đối số, tra về logarit tự nhiên của x(cơ số e)(base điền số vào ví gụ logait 2 cơ số x)
  + math.pow(x,y): trả về x lũy thừa y (x**y)
  + math.sqrt(x): căn bậc2
  VD: math.pi (=3.141592...)
      math.e (=2.718281...)
     
"""

import math #thư viện để sử dụng các số trên
x = float(input("x: "))
print ("|x|= ", math.fabs(x))
print ("sprt(x)= ", math.sqrt(x))
print ("exp(x)= ", math.exp(x))
print ("pi= ", math.pi)
print("ciel= ", math.ceil(x))
print("floor(x)= ", math.floor(x))
print("sin(x)= ", math.sin(x))

"""
VIDEO 13
TOÁN TỬ ĐIỀU KIỆN
    [trả về khi điều kiện đúng] if [điều kiện] else [điều kiệ trả về khi sai]
CÂU LỆNH RẼ NHÁNH IF....ELSE TRONG BYTHON

"""

#vd về toán tử điều kiện
x= input("nhập vào x = ")
x = int(x)
kq = "chẵn" if (x%2==0) else "lẻ"
print (x,"là số",kq)

#vd về câu lệnh rẽ nhánh
x = input('nhập vào số nguyên x: ')
x = int(x)
if x > 0:
    print (x,"là số dương")

if x%2==0:
    print(x, "là số chẵn")
else:
    print(x,"là số lẻ")
print('kết thúc chương trình')

#vd về câu lệnh điều kiện (thuật toán lòng nhau)
x = float(input("nhập vào số điểm của bạn: "))
if x >= 9.0:
    print("xếp loại: xuất sắc")
elif x >= 8:
    print("xếp loại: giỏi")
elif x>=6.5:
    print('xế loại: khá')
elif x >=5:
    print("xếp loại: trung bình")
else:
    print("xếp loại: yếu")