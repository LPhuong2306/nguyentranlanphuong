# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:01:54 2024

@author: lanphuong
"""

import math

print("Giải phương trình bậc hai ax^2 + bx + c = 0")
print("Nhập vào số a: ")
a = int(input())
if a == 0:
    print("Vui lòng nhập a khác 0: ")
    a = int(input())

print("Nhập vào số b: ")
b = int(input())

print("Nhập vào số : ")
c = int(input())

delta = b**2 - 4*a*c

if delta < 0:
    print("Phương trình vô nghiệm")

elif delta == 0:
    print("Phương trình có 2 nghiệm kép: x1 = x2 = ", -(b / (2 * a)) )
    
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print ("x1 = " ,  (-b + math.sqrt(delta)) / (2*a))
    print ("x2 = " ,  (-b - math.sqrt(delta)) / (2*a))
    
    
    


    
    
    
    