#Program Berurutan
#Mendeklarasikan variabel
nim = str(input("Masukkan NIM Anda: "))
nama = str(input("Masukkan Nama Anda: "))
uts = int(input("Masukkan Nilai UTS Anda: "))
tugas = int(input("Masukkan Nilai Tugas Anda: "))
uas = int(input("Masukkan Nilai UAS Anda: "))

#Menghitung Total Nilai
total = (uts/100*30) + (tugas/100*20) + (uas/100*50)

#Menampilkan Hasil
print(" Total Nilai Anda adalah: ", total)

#Proses Percabangan
if (total >= 40):
    print ("Selamat", nama, "dengan NIM", nim, "Anda Lulus")
else:
    print ("Maaf", nama, "dengan NIM", nim, "Anda Tidak Lulus")

#Perulangan dengan For
for i in range (5):
    #Statement didalam perulangan
    print("Belajar python itu mudah dan menyenangkan")