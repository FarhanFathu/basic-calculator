def calculator (first,second,operasi) :
    if operasi == "+":
        return first + second
    elif operasi == "-":
     return first - second
    elif operasi == "*":
        return first * second
    elif operasi == "/":
        if second != 0:
            return first / second 
    elif operasi == "pangkat":
       return first ** second
    else:
     return  "ERROR"
     

while True:
   print(f"\n WElCOME in Basic Calculator")
   first = float(input("Masukkan Angka ke 1 : "))
   second = float(input("Masukkan Angka ke 2 : "))
   operasi =  input("Masukkan Jenis Kalkulator (+,-,*,/,pangkat) : ")
   hasil = calculator(first,second,operasi)
   print(f"\nHasil dari {first} di {operasi} dengan {second} adalah {hasil}")


   Clear = input(f"\nClear All? (YES/NO) : ").strip().upper()
   if Clear != "YES":
      print(f"\nTHANKS")
      break


