# Kalkulator Sederhana Python

print("KALKULATOR SEDERHANA")
print("====================")

# Input angka pertama
angka1 = float(input("Masukkan angka pertama: "))

# Input operasi
print("Pilih operasi:")
print("+ untuk penjumlahan")
print("- untuk pengurangan")
print("* untuk perkalian")
print("/ untuk pembagian")
operasi = input("Masukkan operasi (+, -, *, /): ")

# Input angka kedua
angka2 = float(input("Masukkan angka kedua: "))

# Hitung hasil
if operasi == '+':
    hasil = angka1 + angka2
    print(angka1, "+", angka2, "=", hasil)
elif operasi == '-':
    hasil = angka1 - angka2
    print(angka1, "-", angka2, "=", hasil)
elif operasi == '*':
    hasil = angka1 * angka2
    print(angka1, "*", angka2, "=", hasil)
elif operasi == '/':
    if angka2 == 0:
        print("Error: Tidak bisa membagi dengan nol!")
    else:
        hasil = angka1 / angka2
        print(angka1, "/", angka2, "=", hasil)
else:
    print("Operasi tidak valid!")

print("Selesai!")