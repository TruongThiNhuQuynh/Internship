hoc_bai = "học bài không nản\n"
hoc_bai_10 = hoc_bai*10
print(hoc_bai_10)

chuoi_1 ="xin chào bạn"
chuoi_2 = "xin chào"
chuoi_3 = "quỳnh"
#kiểm tra chuỗi có thuộc chuỗi
if chuoi_2 in chuoi_1:
    print("chuỗi 2 là chuỗi con của chuỗi 1")
else:
    print("chuỗi 2 không phải là tập con của chuổi 1")
if chuoi_3 in chuoi_1:
    print("chuỗi 3 là tập con của chuỗi 1")
else:
    print("chuỗi 3 không phải là tập con của chuỗi 1")

#cộng chuỗi
c4 = chuoi_1 +" " + chuoi_3
print(c4)

#viết hoa chứ đầu chuỗi
s = "hôm nay đi học anh"
s = str.capitalize(s)
print(s)
#viết hoa toàn bộ chuỗi 
s = str.upper(s)  #chú ý
print(s)
#viết thường toàn ộ
s = str.lower(s)
print(s)

#tìm và đêm số lượng chuỗi con
c = "lập trình bython là xu hướng hiện nay. Bạn nên học lập trình bython"
print(c.find("bythonX")) #trả về trừ 1 nếu ko tìm thấy
print(c.find("bython"))  #kq: 10(vị trí thứ 10)
print(c.count("bython")) #kq: 2

#thay thế
c = c.replace("bython","BYTHON")
print(c)
#cắt chuỗi thành 1 list
list1 = c.split(" ") # khi nào có dấu cách thì cắt 
print (list1)
list2 = c.split (".")
print (list2)