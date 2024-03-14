bil1 = int(input("masukan bilangan 1 :"))
bil2 = int(input("masukan bilangan 2 :"))
bil3 = int(input("masukan bilangan 3 :"))

if bil1 < bil2 and bil2 <= bil3:
    bil = "bilangan 1 lebih kecil"
elif bil2 < bil3 and bil3 <= bil1:
    bil = "bilangan 2 lebih kecil"
elif bil3 < bil1 and bil1 <= bil2:
    bil = "bilangan 3 lebih kecil"
else :
    bil = "sama besar"

print ("nilai",bil,"")
