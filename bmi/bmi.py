tinggi = float(input("masukan tinggi baadan(m): "))
berat = int(input("masukan berat badan(kg): "))
bmi = berat / (tinggi*tinggi)
print ("bmi anda: ",bmi)
if bmi < 18.5:
    keterangan = "berat badan kurang"
elif bmi >=18.5 and bmi <= 22.9:
    keterangan = "berat badan normal"
elif bmi >= 23 and bmi <= 29.9:
    keterangan = "berat badan berlebih"
else:
    keterangan = "obesitas"
print ("keteranan: ",keterangan)