""" เเปลงเลขฐาน 2 เป็นฐาน 16 (ใช้วิธีตามGoogle แปลงเป็นฐาน10แล้วค่อยเเปลงฐาน10เป็นฐาน16)"""
"""
แปลงฐาน 10 เป็น ฐาน 16
เอา2มาหาร ถ้าไม่ลงตัวก็แสดงว่าเลขฐาน2ตัวแรกเป็น1 ถ้าลงตัวก็เป็น0 เพราะฐาน2มีแค่0กับ1
หาร2ให้เลขฐาน10ลดไปเรื่อยจนเหลือ0 ละก็มันต้องอ่านกลับจากหลังมาหน้าเลยreveresข้อความ
"""
def Binary_to_Decimal(Binary): # แปลงฐาน 2 เป็นฐาน 10
    Binary = str(Binary)
    Reversed_Number = ""
    N = len(Binary)-1
    while N>=0:
        Reversed_Number += Binary[N]
        N-=1

    Decimal = 0
    for i in range(len(Reversed_Number)):
        if Reversed_Number[i] == "1":
            Decimal += 2**i
    return Decimal

"""
แปลงฐาน 10 เป็น ฐาน 16 
ด้วยการหารเอาเศษมาต่อกันเรื่อยๆ (ไปดูในGoogleนะเราก็อธิบายยาก)
"""
def convert_B_to_Hex(Decimal):
    Decimal = int(Decimal)
    H_all = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    Hexadecimal = ""
    while Decimal > 0:
        if Decimal%16 != 0:
            print(Decimal)
            if Decimal%16 in H_all:
                Hexadecimal = str(H_all.get(Decimal%16)) + Hexadecimal
            else:
                Hexadecimal = str(Decimal%16) + Hexadecimal
        Decimal //= 16
    return Hexadecimal


Binary = 1010101010
print(f"แปลงเป็นฐาน10 = {Binary_to_Decimal(Binary)}") #ใส่ค่า Binary ในฟังก์ชั่นแปลงเป็นฐาน10
print(f"แปลงเป็นฐาน16 = {convert_B_to_Hex(Binary_to_Decimal(Binary))}") # ใส่ค่าฐาน10ที่แปลงเป็นฐาน16