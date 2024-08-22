# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 19:51:20 2024

@author: lanphuong
"""

import random

def keo_bua_bao():

  lua_chon = ["kéo", "búa", "bao"]

  nguoi_choi = input("Bạn chọn gì? (kéo, búa, bao): ").lower()

  may_choi = random.choice(lua_chon)

  print(f"Bạn chọn: {nguoi_choi}")
  print(f"Máy chọn: {may_choi}")

  if nguoi_choi == may_choi:
    return "Hòa!"
  elif (nguoi_choi == "kéo" and may_choi == "bao") or \
       (nguoi_choi == "búa" and may_choi == "kéo") or \
       (nguoi_choi == "bao" and may_choi == "búa"):
    return "Bạn thắng!"
  else:
    return "Máy thắng!"

ket_qua = keo_bua_bao()
print (ket_qua)

