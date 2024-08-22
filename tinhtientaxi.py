# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 19:49:33 2024

@author: lanphuong
"""

def tinh_tien_taxi(km):
    # Giá cho 1 km đầu tiên
    gia_km_dau = 20000

    # Giá từ km thứ 2 đến km thứ 3
    gia_km_2_3 = 13000

    # Giá từ km thứ 4 đến km thứ 8
    gia_km_4_8 = 12000

    # Giá từ km thứ 9 trở đi
    gia_km_tu_9 = 10000

    # Tính tổng tiền
    tong_tien = 0

    if km <= 1:
        tong_tien = gia_km_dau
    elif km <= 3:
        tong_tien = gia_km_dau + (km - 1) * gia_km_2_3
    elif km <= 8:
        tong_tien = gia_km_dau + 2 * gia_km_2_3 + (km - 3) * gia_km_4_8
    else:
        tong_tien = gia_km_dau + 2 * gia_km_2_3 + 5 * gia_km_4_8 + (km - 8) * gia_km_tu_9

    # Giảm giá nếu đi hơn 100 km
    if km > 100:
        tong_tien *= 0.92  # Giảm 8%

    return tong_tien

# Nhập số km quãng đường đi được
so_km = float(input("Nhập số km quãng đường đi được: "))
tong_tien_taxi = tinh_tien_taxi(so_km)
print(f"Tổng tiền taxi: {tong_tien_taxi:.1f} đồng")
