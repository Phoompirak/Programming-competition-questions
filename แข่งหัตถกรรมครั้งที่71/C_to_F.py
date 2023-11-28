"""1.รับค่า2ค่า หลูบ xถึงy เเปลงC°เป็นF°ของรอบที่กำลังหลูบ"""
def find_f(c):
    F = 1.8*c+32 # สูตรเเปลงองศาเป็ฯฟาเรนไฮ
    return F

x, y = int(input("x:")), int(input("y:"))
for i in range(x, y+1):
    print(f"C = {i}, F = {find_f(i)}") # แสดงผลค่า i ก่อนและหลังแปลงเป็นฟาเรนไฮ