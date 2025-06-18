"""
video 16
XÁC ĐỊNH TAM GIÁC TÌNH CHU VI VÀ DIỆN TÍCH CỦA TAM GIÁC
   1. Nhập 3 điểm trên hệ trục tọa độ:
   2. nếu tạo thành tam giác:
       + xuất ra chu vi của tam giác
       + xuất ra diện tích của tam giác
"""
import math
# nhập dữ liệu
xA = float(input("nhập vào xA:"))
yA = float(input("nhập vào yA:"))
xB = float(input("nhập vào xB:"))
yB = float(input("nhập vào yB:"))
xC = float(input("nhập vào xC:"))
yC = float(input("nhập vào yC:"))

ab = math.sqrt((xB-xA)**2 + (yB-yA)**2)
ac = math.sqrt((xC-xA)**2 + (yC-yA)**2)
bc = math.sqrt((xC-xB)**2 + (yC-yB)**2)
if (ab + bc > ac) and (ab + ac > bc) and (ac + bc > ab):
    print("tạo thành tam giác")
    #tính chu vi
    C = ab + ac +bc
    print("chu vi của tam giác ABC là:", C)
    #tính diện tích
    p = (ab + ac + bc)/2
    S = math.sqrt(p*(p-ab)*(p-ac)*(p-bc))
    print ("diện tích của tam giác ABC là: ",S)
else:
    print("không phải là tam giác")

