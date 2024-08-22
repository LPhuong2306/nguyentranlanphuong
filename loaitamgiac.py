# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 20:13:34 2024

@author: lanphuong
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

if a + b > c and a + c > b and b + c > a:
    
  if a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b:
    loaiTamGiac = 'vuong'

  elif a==b and b==c:
    loaiTamGiac = 'deu'

  elif a==b or a==c or b==c:
    loaiTamGiac = 'can'

  elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:   
    loaiTamGiac = 'tu'

  else:
    loaiTamGiac = 'nhon'
  print('{}, {}, {} la ba canh cua mot tam giac {}'.format(a, b, c, loaiTamGiac))
else:
  print("{}, {}, {} khong phai la ba canh cua mot tam giac".format(a, b, c))