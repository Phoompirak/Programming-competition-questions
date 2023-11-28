def Binary_to_Decimal(Binary):
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
# print(convert_B_to_Hex(Binary))
print(Binary_to_Decimal(Binary))
print(convert_B_to_Hex(Binary_to_Decimal(Binary)))