# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 18:43:38 2024

@author: lanphuong
"""

print("Giải phương trình bậc nhất ax + b = 0")
print("Nhập vào số a:")
a = int(input())

if a == 0:
    print("Vui lòng nhập a khác 0: ")
    a = int(input())

print("Nhập vào số b: ")
b = int(input())
print("Nghiệm của phương trình là x = ", (- b / a))


