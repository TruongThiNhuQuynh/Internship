"""
video 5
NHẬP VÀO ( LỆNH INPUT)
"""

input("nhập vào một con số: ") # nhập vào một số 
a = input ("nhập vào a: ")  # nhập vào 1 số a và in ra nó
print ("a = {0}".format(a))

ho = input ("Nhập họ của bạn: ") 
ten = input ("nhập tên của bạn: ")
print( "Họ tên của bạn là: {0} {1} ".format(ho,ten))
print("họ tên của bạn là:", ho, ten)  # 2 câu lệnh trên có kết quả giống nhau


"""
video 6
BIẾN, HẰNG SỐ VÀ TỪ KHÓA TRONG BYTHON
 VD: x=5 , ban đầu tạo 1 biến có 5 giá trị
     y=5, ban đầu y có giá trị là 5
     y=10, y được thay dổi giá trị là 10
 Hằng sô
    "viết hoa" để tránh bị nhầm lẫn với các biến khác 
    VD: PI=3.14
        print(PI) #in ra 3.14
    VD: import math
        print(math.pi) # in ra 3.1415...
 lưu ý khi đặt tên biến và hằng số
    chữ cái: "a->z" or "A->Z"
    chứ số: "0->9"
    dấu gạch dưới "_" để đặt cho tên biến hoặc hằng số
 - không sử dụng từ kháo làm tên biến:
       false         else
       true          not
       none          or
       and           from
       as            in .....

"""
#gán giá trị cho 1 biến
x=5
x=10
print(x) #in ra kết quả 10
#gán giá trị cho nhiều biến cùng lúc
x, y, z = 2, 4, "như quỳnh"
print(x)
print(y)
print(z) #kết quả:  2  4   như quỳnh.  kết quả xuống dòng
print(x, y,z) #kết quả: 2 4 như quỳnh. kết qur ko xuống dòng

#hằng số
PI=3.14
print(PI)
import math
print(math.pi)
