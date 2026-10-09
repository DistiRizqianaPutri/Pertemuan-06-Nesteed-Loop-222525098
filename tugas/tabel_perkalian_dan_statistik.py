
print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi n dengan while
while n <= 0:
    print("Input harus bilangan positif!")
    n = int(input("Masukkan n kembali: "))

# Inisialisasi statistik
total_keseluruhan = 0
counter_genap = 0

# Membuat tabel perkalian dan statistik
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(hasil, end="\t")

        total_baris += hasil
        total_keseluruhan += hasil

        if hasil % 2 == 0:
            counter_genap += 1

    print(f"| Total baris {i} = {total_baris}")

# Menampilkan statistik
print("\nStatistik:")
print(f"Total keseluruhan = {total_keseluruhan}")
print(f"Banyak bilangan genap = {counter_genap}")
