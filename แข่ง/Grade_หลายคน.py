def all_people_grade(name={}): # ฟังก์ชั่นวนหลูบหาgradeรายบุคคล
    for k, v in name.items(): # ดึงkey, value ในNameมาวนหลูบ
        print(f"Name = {k} , Grade = {find_grade(v)}") # แสดงผลชื่อพร้อมgrade ที่คำนวณด้วยฟังก์ชั่นfind_grade
    return "\nจบการคำนวณGrade"

def find_grade(score): # ฟังก์ชั่นคำนวณGrade
    grade = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0] # List รวมgrade
    # เช็คไปทีละเขื่อนไง
    if score >= 80 and score <= 100: # 4.0
        return grade[0]
    elif score >= 75 and score <= 79: # 3.5
        return grade[1]
    elif score >= 70 and score <= 74: # 3.0
        return grade[2]
    elif score >= 65 and score <= 69: # 2.5
        return grade[3]
    elif score >= 60 and score <= 64: # 2.0
        return grade[4]
    elif score >= 55 and score <= 59: # 1.5
        return grade[5]
    elif score >= 50 and score <= 54: # 1.0
        return grade[6]
    else: # 0.0
        return grade[7]

People = int(input("People :")) # รับค่าจำนวนคนที่จะป้อน
Names = dict() # Dictionary ไว้เก็บชื่อ, คะแนน
for i in range(People): # วนหลูบตามจำนวนคน
    # ป้อนชื่อ, คะแนนกลางและปลายภาคที่บวกกันแล้ว
    Name = {input("Name :"):int(input("Score 1:")) + int(input("Score 2:"))}
    Names.update(Name) # เพิ่มข้อมูลที่รับมาใน Names

print(all_people_grade(Names)) # แสดงผลการคำนวณGradeของทุกคน