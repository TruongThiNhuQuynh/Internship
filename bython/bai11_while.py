"""
VIDEO 21
VÒNG LẶP WHILE

#yêu cầu người dùng nhập vào một con số n>0. nếu nhập sai thì yêu cầu người dùng nhập lại
n = -1
while (n<=0):
    n = int(input("nhập vào n: "))

i = 0
tong = 0
while (i<=n):
    tong+=i
    i+=1
print("tổng = ", tong)
"""

#Chuyển đổi số từ thập phân sang nhị phân
n=-1
while (n<=0):
    n = int(input("nhập số thập phân(n>0): "))
x=n
ketqua = ""
while (n>0):
    ketqua = str(n%2) + ketqua
    print("n%2=", n%2)
    n = n//2
    print ("n = ", n)
   
print("kết quả là: ",ketqua)
