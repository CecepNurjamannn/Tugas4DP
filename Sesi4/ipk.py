def bobot(nilai):
    if nilai >=90 and nilai <=100 :
        return 4
    elif nilai >=85 and nilai <=89 :
        return 3.75
    elif nilai >=80 and nilai <=84:
        return 3.5
    elif nilai >=75 and nilai <=79:
        return 3.25
    elif nilai >=70 and nilai <=74:
        return 3
    elif nilai >=65 and nilai <=69:
        return 2.75
    elif nilai >=60 and nilai <=64:
        return 2.5
    elif nilai >=55 and nilai <=59:
        return 2.25
    elif nilai >=50 and nilai <=54:
        return 2
    elif nilai >=45 and nilai <=49:
        return 1.75
    elif nilai >=40 and nilai <=44:
        return 1.5
    elif nilai >=35 and nilai <=39:
        return 1.25
    elif nilai >=30 and nilai <=34:
        return 1
    elif nilai <=30:
        return 0
    else :
        "nilai yang di input salah"


algoritma = float(input("masukan nilai Algoritma :"))
sks_algoritma = float(input("masukan jumlah sks Algoritma :"))
print("Bobot nilai Algoritma anda :",bobot(algoritma))

perancangan_objek = float(input("masukan nilai Perancangan Objek :"))
sks_perancangan_objek = float(input("masukan jumlah sks Perancangan Objek :"))
print("Bobot nilai perancangan objek anda :",bobot(perancangan_objek))

kalkulus = float(input("masukan nilai Kalkulus :"))
sks_kalkulus = float(input("masukan jumlah sks Kalkulus :"))
print("Bobot nilai kalkulus anda :",bobot(kalkulus))

etika_profesi = float(input("masukan nilai Etika Profesi :"))
sks_etika_profesi = float(input("masukan jumlah sks Etika Profesi :"))
print("Bobot nilai etika profesi anda :",bobot(etika_profesi))

databases = float(input("masukan nilai Databases :"))
sks_databases = float(input("masukan jumlah sks Databases :"))
print("Bobot nilai databases anda :",bobot(databases))

english = float(input("masukan nilai English :"))
sks_english = float(input("masukan jumlah sks English :"))
print("Bobot nilai english anda :",bobot(english))


total_sks = sks_algoritma + sks_perancangan_objek + sks_kalkulus + sks_etika_profesi + sks_databases + sks_english

total_nilai_algoritma = bobot(algoritma) * sks_algoritma
total_nilai_Perancangan_Objek = bobot(perancangan_objek) * sks_perancangan_objek
total_nilai_kalkulus = bobot(kalkulus) * sks_kalkulus
total_nilai_etika_profesi = bobot(etika_profesi) * sks_etika_profesi
total_nilai_databases = bobot(databases) * sks_databases
total_nilai_english = bobot(english) * sks_english

total_semua_nilai = total_nilai_algoritma + total_nilai_Perancangan_Objek + total_nilai_kalkulus + total_nilai_etika_profesi + total_nilai_databases + total_nilai_english  # type: ignore

ipk = total_semua_nilai / total_sks

print("IPK Anda semester ini adalah :",ipk,"")