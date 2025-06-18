"""
video 9
CÁC PHÉP TOÁN SỐ HỌC TRONG BYTHON
   - các phép tians tròng bython
        + cộng (+)
        + trừ (-)
        + nhân (*)
        + chia (/)
        + chia lấy phần dư (%)
        + mũ(**)
        + chia lấy phần nguyên (//)
   --> khi nhập dữ liệu từ bàn phím " kiểu str" nên ta cần phải ép kiểu dữ liệu lại nới tính toán được
"""

a = input("nhập vào số a: ")
a= float(a)
print("kiểu dữ liệu của a: ", type(a))
b = input("nhập vào số b: ")
b= float(b)
print("kiểu dữ liệu của b: ", type(b))

print("{0} + {1} = {2}".format(a,b,a+b))
print("{0} - {1} = {2}".format(a,b,a-b))
print("{0} * {1} = {2}".format(a,b,a*b))
print("{0} / {1} = {2}".format(a,b,a/b))
print("{0} ** {1} = {2}".format(a,b,a**b))
print("{0} // {1} = {2}".format(a,b,a//b))
print("{0} % {1} = {2}".format(a,b,a%b))


"""
video 10
SO SÁNH VÀ LOGIC TRONG LẬP TRONG LẬP TRÌNH BYTHON
  -SO SÁNH
    + hớn hơn  (>)
    + bé hơn  (<)
    + bằng (==)
    + khác, không băng  (!=)
    + hớn hơn or bằng  (>=)
    + bé hơn or bằng   (<=)
  -LOGIC
    + and : trả về giá trị True nếu tất cả các toán hạng là True   
    + or : trả về giá trị True nếu có ít nhất 1 toán hang True
    + not : phủ định (True-->false, false -->True) 

"""
#ví dụ về so sánh
#True or False (máy sẽ tự trả về kiểu bool)
x = int(input("x = "))
y = int(input("y = "))
print("{0}<{1} là {2}".format(x, y, x<y))
print("{0}>{1} là {2}".format(x, y, x>y))
print("{0}=={1} là {2}".format(x, y, x==y))
print("{0}!={1} là {2}".format(x, y, x!=y))
print("{0}<={1} là {2}".format(x, y, x<=y))
print("{0}>={1} là {2}".format(x, y, x>=y))

#ví dụ về logic
z = int(input("z: "))
print ("({0}<{1}) and ({2}<{3})={4}".format(x,y,y,z, (x<y) and (y<z)))
print ("({0}<{1}) or ({2}<{3})={4}".format(x,y,y,z, (x<y) or (y<z)))
print ("not({0}>{1}) ={2}".format(x,z,  not (x>z)))

"""
VIDEO 11
TOÁN TỬ GÁN
   +  "=" giống  "a=9"
   +  "+=" giống  "a=a+9"
   +  "-=" giống  "a=a-9"  #9 có thể thay đổi bằng số khác
   +  "*=" giống  "a=a*9"
   +  "/=" giống  "a=a/9"
   +  "%=" giống  "a=a%9"
   +  "//="  giống  "a=a//9"
   +  "**=" giống  "a=a**9"
     
"""
