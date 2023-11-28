"""
2.คำนวณค่าจอดรถ
  ไม่เกิน15นาที จอดฟรี
  15นาที-3ชม. ชม.ละ10บาท เศษนับเป็น1ชม.
  4ชม.- 6ชม. ชม.ละ10บาท เหมือนกัน
  มากกว่า6ชม. เหมาจ่าย 200บาท

  เศษนาที ปัดเป็นชั่วโมง
"""
import math # เพิ่ม math มาปัดเศษขึ้นเฉยๆ

def find_time(time, h_or_m): # ฟังก์ชั่น
    if h_or_m == "h":
        time = time*60
    return find_pay(time) # ส่งค่าหลังจากนำtimeไปคำนวณในฟังก์ชั่น find_pay เสร็จ

def find_pay(time): # ฟังก์ชั่นคำนวณว่าต้องจ่ายค่าจอดรถกี่บาท
    if time < 0:
        return "เวลาไม่ติดลบ"
    elif time <= 15:
        return "จอดฟรี"
    elif time > 15 and time <= 360: # 15นาที-6ชั่วโมง จ่ายชั่วโมงละ 10 บาทเหมือนกัน
        return math.ceil(time/60)*10 # หารปัดเศษขึ้นเพราะเศษนาทีนับเป็น 1ชั่วโมง
    else:
        return "เหมาจ่าย 200"

Time = float(input("Time :")) # รับค่าเวลา
h_or_m = input("Hour or Minute (H or M):") # รับค่าหน่วยเวลา ชั่วโมงหรือนาที
print(f"ต้องจ่าย = {find_time(Time, h_or_m)}") # แสดงผลฟังก์ชั่น find_time