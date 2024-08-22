"""
Created on Thu Aug 15 19:11:08 2024

@author: lanphuong
"""

def is_leap_year(year):
  
  return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

def is_valid_date(date_str):
  
  try:
    day, month, year = map(int, date_str.replace('-', '/').split('/'))
    if year < 0:
      return False
    if month < 1 or month > 12:
      return False
    if day < 1 or day > 31:
      return False
    if month in [4, 6, 9, 11] and day > 30:
      return False
    if month == 2:
      if is_leap_year(year):
        return day <= 29
      else:
        return day <= 28
    return True
  except ValueError:
    return False

# Nhập ngày tháng năm từ người dùng
date_str = input("Nhập ngày tháng năm (dd/mm/yyyy hoặc dd-mm-yyyy): ")

# Kiểm tra và hiển thị kết quả
if is_valid_date(date_str):
  print("Ngày tháng năm hợp lệ.")
  day, month, year = map(int, date_str.replace('-', '/').split('/'))
  if is_leap_year(year):
    print(f"Năm {year} là năm nhuận.")
  else:
    print(f"Năm {year} không phải là năm nhuận.")
else:
  print("Ngày tháng năm không hợp lệ.")