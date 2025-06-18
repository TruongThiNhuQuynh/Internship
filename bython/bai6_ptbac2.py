"""
video 15
GIẢI PHƯƠNG TRÌNH BẬC 2

"""
import math
print("giải phương trình ax^2 + bx +c = 0")
a = float(input("nhập a = "))
b = float(input("nhập b = "))
c = float(input("nhập c = "))

if a == 0 :
    print("không phải phương trình bậc 2")
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("phương trình vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print("phương trình có nghiện kép x = ",x)
    else:
        x1 = (-b - math.sqrt(delta))/(2*a)
        x2 = (-b + math.sqrt(delta))/(2*a)
        print("phương trình có 2 nghiệm x1={0} và x2={1}".format(x1,x2))

        
