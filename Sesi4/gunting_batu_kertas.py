pemain1 = input("masukan pilihan pemain 1 (gunting/batu/kertas) :")
pemain2 = input("masukan pilihan pemain 2 (gunting/batu/kertas) :")

if pemain1 == pemain2 :
    print ("hasil seri")
elif pemain1 == "batu" :
    if pemain2 == "gunting" :
        print ("pemain 1 menang")
    else :
        print ("pemain 2 menang")
elif pemain1 == "gunting" :
    if pemain2 == "kertas" :
        print ("pemain 1 menang")
    else: 
        print ("pemain 2 menang")
elif pemain1 == "kertas" :
    if pemain2 == "batu" :
        print ("pemain 1 menang")
    else :
        print ("pemain 2 menang")
else :
    print ("input yang anda berikan salah")

