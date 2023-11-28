"""
2.คำนวณค่าจอดรถ
  ไม่เกิน15นาที จอดฟรี
  15นาที-3ชม. ชม.ละ10บาท เศษนับเป็น1ชม.
  4ชม.- 6ชม. ชม.ละ10บาท เหมือนกัน
  มากกว่า6ชม. เหมาจ่าย 200บาท
"""
import math # เพิ่ม math มาปัดเศษขึ้นเฉยๆ

def find_time(time, h_or_m): # ฟังก์ชั่น
    if h_or_m == "h":
        time = time*60
    return find_pay(time)

def find_pay(time): # ฟังก์ชั่นคำนวณว่าต้องจ่ายค่าจอดรถกี่บาท
    if time < 0:
        return "เวลาไม่ติดลบ"
    elif time <= 15:
        return "จอดฟรี"
    elif time > 15 and time <= 360:
        return math.ceil(time/60)*10
    else:
        return "เหมาจ่าย 200"

Time = float(input("Time :"))
h_or_m = input("Hour or Minute :")
print(f"ต้องจ่าย = {find_time(Time, h_or_m)}")