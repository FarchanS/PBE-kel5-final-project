while True:
    try:
        a = float(input("masukkan angka ke1 = "))
        break
    except:
        print("MASUKKAN ANGKA")
operator = input("operator(+,-,x,/)= ")
while operator !='+' and operator !='-' and operator !='x' and operator !='/':
    print("masukkan operator bro")
    operator = input("operator = ")
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
