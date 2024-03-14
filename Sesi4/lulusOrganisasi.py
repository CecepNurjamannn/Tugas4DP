jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")
berat_badan = float(input("Masukkan berat badan (kg): "))
tinggi_badan = float(input("Masukkan tinggi badan (cm): "))
usia = int(input("Masukkan usia (tahun): "))
nilai_akademis = float(input("Masukkan nilai rata-rata akademis: "))
keahlian = input("Masukkan keahlian (Menembak/Memanah/Berkuda): ")
cacat_tubuh = input("Apakah memiliki cacat tubuh (Ya/Tidak): ")

# Memeriksa kelayakan berdasarkan jenis kelamin
if jenis_kelamin == "P":
    if berat_badan >= 45 and berat_badan <= 50 and tinggi_badan >= 165 and usia < 20:
        lulus_kriteria_1 = True
    else:
        lulus_kriteria_1 = False
elif jenis_kelamin == "L":
    if berat_badan <= 70 and tinggi_badan >= 170 and usia < 25:
        lulus_kriteria_1 = True
    else:
        lulus_kriteria_1 = False
else:
    print("Jenis kelamin tidak valid.")
    

# Memeriksa kelayakan berdasarkan nilai akademis
if nilai_akademis >= 90 and usia < 30:
    lulus_kriteria_2 = True
else:
    lulus_kriteria_2 = False

# Memeriksa kelayakan berdasarkan keahlian
if keahlian.lower() in ["menembak", "memanah", "berkuda"]:
    lulus_kriteria_3 = True
else:
    lulus_kriteria_3 = False

# Memeriksa kelayakan berdasarkan cacat tubuh
if cacat_tubuh.lower() == "tidak":
    lulus_kriteria_4 = True
else:
    lulus_kriteria_4 = False

# Menentukan kelulusan
if (lulus_kriteria_1 or lulus_kriteria_2) and lulus_kriteria_3 and lulus_kriteria_4:
    print("anda dinyatakan LULUS seleksi anggota organisasi .")
else:
    print("anda dinyatakan TIDAK LULUS seleksi anggota organisasi .")
