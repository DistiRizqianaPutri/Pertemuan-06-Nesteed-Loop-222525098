
# Pertemuan 06 Nested Loop Python
# Nama: Disti Rizqiana Putri
# NIM: 2225250098
# Kelas: 3E

print("Tabel Perkalian dan Statistik")

# Input dan validasi
while True:
    try:
        n = int(input("Masukkan n: "))
        if n > 0:
            break
        else:
            print("Input harus bilangan positif!")
    except ValueError:
        print("Input tidak valid! Masukkan bilangan bulat.")

# Inisialisasi statistik
total_keseluruhan = 0
counter_genap = 0

# Nested loop untuk tabel perkalian
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(f"{hasil:4}", end="")

        total_baris += hasil
        total_keseluruhan += hasil

        if hasil % 2 == 0:
            counter_genap += 1

    print(f" | Total baris {i} = {total_baris}")

# Menampilkan statistik
print("\n=== Statistik ===")
print(f"Total keseluruhan = {total_keseluruhan}")
print(f"Banyak bilangan genap = {counter_genap}")
print(f"Banyak seluruh hasil perkalian = {n * n}")
