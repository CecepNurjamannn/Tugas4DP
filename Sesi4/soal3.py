bil1 = int(input("masukan bilangan 1 :"))
bil2 = int(input("masukan bilangan 2 :"))
bil3 = int(input("masukan bilangan 3 :"))

if bil1 == bil2 and bil3 < bil1 :
    print ("ada dua bilangan",bil1,"yang lebih besar dari bilangan",bil3)
elif bil1 > bil2 and bil2 > bil3 :
    print ("bilangan",bil1,"lebih besar dari",bil2,"dan",bil3)
elif bil2 == bil3 and bil1 < bil2 :
    print ("ada dua bilangan",bil2,"yang lebih besar dari bilangan",bil1)
elif bil2 > bil3 and bil3 > bil1 :
    print ("bilangan",bil2,"lebih besar dari",bil3,"dan",bil1)
elif bil3 == bil1 and bil2 < bil3 :
    print ("ada dua bilangan",bil3,"yang lebih besar dari bilangan",bil2)
elif bil3 > bil1 and bil1 > bil2 :
    print ("bilangan",bil3,"lebih besar dari",bil1,"dan",bil2)
else :
    print ("semua bilangan sama")


