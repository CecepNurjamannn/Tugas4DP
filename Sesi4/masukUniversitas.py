nama = input("masukan nama anda :")
tempat_lahir = input("tempat lahir :")
tanggal_lahir = int(input("masukan tanggal lahir :"))
tahun_lahir = int(input("masukan tahun lahir :"))
jenis_kelamin = input("jenis kelamin (L/P) :")

English = int(input("masukan nilai English :"))
MTK = int(input("masukan nilai MTK :"))
Indonesia = int(input("masukan nilai Indonesia :"))

nilai_rata = (English+MTK+Indonesia) / 3
usia = 2024 - tahun_lahir 

if usia < 25 :
    if nilai_rata >=80 and jenis_kelamin == "L" :
        print ("anda disarankan masuk ke Teknik Informatika")
    elif nilai_rata >=80 and jenis_kelamin == "P" :
        print ("anda disarankan masuk ke Sistem Informasi")
    else :
         print ("anda disarankan masuk ke Desain Komunikasi Visual")
else :
    print ("usia anda",usia,"tidak lulus melebihi batas usia")

print ("nilai rata-rata :",nilai_rata,"")
