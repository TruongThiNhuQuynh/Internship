
#nhập dữ liệu
a = input("nhap vao a: ")
#xử lý
a = int(a)
b = a + 2
# hoặc b = int(a) +2
# xuất dữ liệu
print(b)

"""
video 3
- không cần dấu ";" ở cuối câu lệnh
- chương trình con thì thụt lề vào trong (còn trong ngôn ngữ khác thì dùng "{}")
- nhấn "TAB" để thụt lề sang phải tạo chương trình còn
video 4
- xuất dữ liệu
   + print (object(s), sep= separator, end=end, file=file, flush=slush)
     trong đó: object (s) là đối thượng dữ liệu được xuất
               sep: ngăn cách 
               end: kết thúc 
               file: tên tập tin
               flush: đẩy dữ liệu 
"""
print(7); print("Hello world") # dùng dấu ";" để ngân cahs 2 câu lệnh trog 1 dòng
print("Xin", "chào", "bạn", "Quỳnh") # in ra câu Xin chào bạn Quỳnh
print("Xin", "chào","bạn", "Quỳnh", sep=",") # câu lệnh  ( sep="," in ra dấu "," ngăn cách giữa các từ trên)
print("Xin chào", end =": ") # end= ":" kết thúc câu lệnh trên bằng dấu 2 ":" rồi in câu lệnh dưới sau dấu ":" 
print("Quỳnh") # kết quả: "Xin chào: Quỳnh"
print('Tên = {0}, Họ = {1}'.format('Quỳnh', 'Trương')) #kết quả in ra: Tên=Quỳnh, Họ = Trương. giống câu lệnh print(%d,x) trong C/C++

