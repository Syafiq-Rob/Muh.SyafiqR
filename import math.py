import math

def hitung_persegi_panjang():
    print("\n=== Hitung Keliling dan Luas Persegi Panjang ===")
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    print(f"Keliling: {keliling}")
    print(f"Luas: {luas}")

def hitung_luas_lingkaran():
    print("\n=== Hitung Luas Lingkaran ===")
    jari_jari = float(input("Masukkan jari-jari: "))
    luas = math.pi * jari_jari ** 2
    print(f"Luas: {luas:.2f}")

def main():
    while True:
        print("\n=== Menu ===")
        print("1. Hitung keliling dan luas persegi panjang")
        print("2. Hitung luas lingkaran")
        print("3. Keluar")
        pilihan = input("Pilih menu (1/2/3): ")

        if pilihan == "1":
            hitung_persegi_panjang()
        elif pilihan == "2":
            hitung_luas_lingkaran()
        elif pilihan == "3":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()