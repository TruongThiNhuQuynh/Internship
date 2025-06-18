"""
video 17
KIỂU DỮ LIỆU LIST TRONG BYTHON
List: dánh sách là chuỗi các mục có thứ tự. nó là một trong những kiểu dữ liệu
được sử dụng nhiều nhất trong bython và linh hoạt. tất cả các mục trong danh sách không cần phải cùng loại
- khai báo một danh sách khá đơn giản. Các mục được phân tách bằng dấu  "," và được đtặ trong "[]"

"""
#tạo list rỗng
emptylist = []

#tạo ra một đối tượng list rỗng 
emptylist1 = list()
print(emptylist)
print(emptylist1)

#tạo ra list dữ liệu
colors = ["red", "green","orange"]
print(colors)

# TẠO DANH SÁCH SINH VIÊN có thứ tự, vị trí các phần tử được đánh dấu từ 0
studentlist = ["Quỳnh", "Thảo", "Phúc", "Hùng"]
print(studentlist[2])  #in ra Phúc
print(studentlist[:])  #in ra tất cả 
print(studentlist[1:2]) #lấy từ vị trí [x,y)--> lấy "Thảo"
print(studentlist[0:2]) #in ra quỳnh thảo

#THÊM PHẦN TỬ VÀO LIST
studentlist.append ("Thiên") #['Quỳnh', 'Thảo', 'Phúc', 'Hùng', 'Thiên']
print(studentlist)  #append:thêm vào cuối
studentlist[len(studentlist):] = ["Thành"] #len là cuối( thêm "Thành vào cuối dánh sách")
print(studentlist)

studentlist.insert(2, "Ngọc") #chèm ngọc vào vị trí số 2
print(studentlist)

#số lượng phần tử có trong list  (len : dộ dài)
print(len(studentlist)) #kq: 7 ( có 7 bạn)

#đếm số lượng phần tử thỏa điều kiện
print("đếm Ngọc: ", studentlist.count("Ngọc")) #kq: 1 vì có 1 ngọc trong danh sách

#xóa tên ra khỏi danh sách
studentlist.remove("Thiên") #vidu: nếu có 2 tên trùng nhau thì xóa tên ở vị trí đầu tiên
print(studentlist)

#kiểm tra phần tử có trong list
if "Ngọc" in studentlist:
    studentlist.remove ("Ngọc")
    print(studentlist)
else:
    print("không có Ngọc ở trong danh sách")

#xóa phần tử ra khỏi bằng vị trí
studentlist.pop(1) #xóa thỏa ra khỏi danh sách
print(studentlist)

#đảo ngược list
studentlist.reverse()
print(studentlist)

#sắp xếp lại theo anpha bê
studentlist.sort()
print(studentlist)

numbers = [1, 5, 9, 3, 6, 3, 6, 8, 3]
numbers.sort()
print(numbers)

#sắp xếp ngược lại
numbers.sort(reverse=True)
print(numbers)

"""
tổng hợp bài học
  - tạo 1 list rỗng:  + emprylist = []  
                      + emptylist = list()
  - tạo 1 list dữ liệu:  + studentlist = ["quỳnh", "thảo", "thành", "hùng"]
  - thêm 1 bạn "thiên" vào cuối danh sách lớp:
            + studentlist.append("thiên")
            + studentlist[len(studentlist)] = ["thiên]
  - chèm 1 bạn "ngọc" vào 1 vị trí bất kì: 
            + studentlist.insert(2,"ngọc")
  - in ra theo thứ tự, vị trí: + print(studentlist[2]) . ỉn thành
                               + print(studentlist[2:4]) . in ra ở vị trí 2,3
                               + print(studentlist[:]) . in ra toàn bộ danh sách
  - đếm số lượng phần tử:
           + print(len(studentlist))
  - đếm số lượng thỏa điều kiện:
           + print("đếm ngọc:", studentlist.cout("ngọc"))
  - kiểm tra phần tử có trong danh sách ko:
           + if "ngọc" in studentlist:
                 print("có ngọc ở trong list)
            else:
                 print("không có ngọc trong danh sách")
  - xóa quỳnh ra khỏi danh sách
        + studentlist.remove("quỳnh")
  - xóa phần tử ra khỏi bằng vị trí" 
        + studentlist.pop(0)
  - đảo ngược list
        + studentlist.reserve()
  - xắp xếp theo ab
        + studentlist.sort()
  - sắp xếp ngược lại:
        + studentlist.sort(reserve=True)
         
"""