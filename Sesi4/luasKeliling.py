import math 

sisi1 = float(input("masukan sisi ke 1 ;"))
sisi2 = float(input("masukan sisi ke 2 ;"))
sisi3 = float(input("masukan sisi ke 3 ;"))

keliling = sisi1 + sisi2 + sisi3

s = keliling / 2

luas = math.sqrt (s* (s - sisi1) * (s - sisi2) * (s - sisi3))

print ("luas segitiga :",luas)
print ("luas keliling :",keliling)


