#no 4 dan 5
nilai = int(input("masukan angka :"))

if nilai ==0 :
    print ("bilangan",nilai)
elif nilai < 0 :
    print ("bilangan",nilai,"adalah negatif")
    if nilai %2 == 0 :
        print ("bilangan",nilai,"adalah bilangan genap")
    else : 
        print ("bilangan",nilai,"adalah bilangan ganjil")
elif nilai > 0 :
    print ("bilangan",nilai,"adalah positif")
    if nilai %2 == 0 :
        print ("bilangan",nilai,"adalah bilangan genap")
    else : 
        print ("bilangan",nilai,"adalah bilangan ganjil")


else :
    print ("salah input")