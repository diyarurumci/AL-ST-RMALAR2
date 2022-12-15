import random
a = 0
b = 0
while b == 0:
     sayi = random.randint(10,99)
     print(sayi)
     if sayi == str(sayi)[::-1]:
         continue
     else:
         b += 1

 
while a == 0 :
    dogruyer_sayac = 0
    yanlısyersayac = 0
    giris = input("Tahmininizi giriniz : ")
    b = int(str(giris)[0])
    c = int(str(giris)[1])
    if  int(giris) > 98 or giris == str(giris)[::-1] :
        print("lütfen nizami bir sayı giriniz")
        continue
    else:
         if b == int(str(sayi)[0]) :
             dogruyer_sayac += 1
         else:
              yanlısyersayac -= 1
         if c == int(str(sayi)[1]):
             dogruyer_sayac += 1 
         else:
             yanlısyersayac -= 1
    print("doğruyer sayacı:",dogruyer_sayac)
     
    print("yanlış yer sayacı :",yanlısyersayac)        
    if dogruyer_sayac == 2 :
        print("tebrikler dopru sayıyı buldunuz")
        break
    
        

    
