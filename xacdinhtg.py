# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:55:46 2024

@author: lanphuong
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    print("Đây là một tam giác")
else:
    print("Không tạo thành tam giác")
    