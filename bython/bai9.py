"""
video18
vòng lặp "for" trong bython

"""
"""
#vòng lặp đi từ 0 đến < n
n = 10
for i in range(n):
    print(i) #in từ 0 đến 9

#tính tổng từ 0 đến n1
n = int(input("nhập n: "))
tong=0
for i in range(n+1):
    tong+=i
print("tổng là: ", tong) #n(n+1)/2

for i in range(0, 12, 3):
    print(i)

#VÒNG LẶP FOR CỦA LISt
studentlist = ["quỳnh", "lan", "hoa", "hùng"]

for studentlist in studentlist:
    print(studentlist)

#hoặc
for i in range(len(studentlist)):
    print(studentlist[i])

"""
# in ra bảng cuur chương 
for i in range(1, 11):
    print("2 x {0} = {1}".format(i, 2*i))

#in ra tất cả bảng cửu chương
for j in range(2, 10):
    print ("bảng cửu chương ", j)
    for i in range (1, 11):
        print("{0} x {1} = {2}". format(j, i, j*i))