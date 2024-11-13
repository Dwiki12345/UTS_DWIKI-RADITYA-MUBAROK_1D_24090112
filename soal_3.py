Jumlah = int(input("Masukan Jumlah Barang : "))
total_barang = 0

for i in range(1,Jumlah + 1):
    harga = int(input(f'Masukan Harga Barang ke-{1}: '))
    total_barang += harga
total = total_barang
print(f'Total Belanjaan : Rp.{total}')
