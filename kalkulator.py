while True:
    try:
        a = float(input("masukkan angka ke1 = "))
        break
    except:
        print("MASUKKAN ANGKA")
while True:
    try:
        operator = input("operator = ")
        if operator !="+" or operator !="-" or operator !="x" or operator !="/":
            break
    except:
        print("masukkan operator")
while True:
    try:
        b = float(input("masukkan angka ke2 = "))
        break
    except:
        print("MASUKKAN ANGKA")

if operator=="+":
    print("hasilnya = ",a + b)
elif operator=="-":
    print("hasilnya = ",a - b)
elif operator=="x":
    print("hasilnya = ",a * b)
elif operator=="/":
    print("hasilnya = ",a / b)
elif operator== "%":
    print("hasilnya = ",a%b)
elif operator== "//":
    print("hasilnya = ",a//b)
else :
    print()