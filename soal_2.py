def pengecekan_tahun_kabisat(tahun):
    return (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0)

tahun = int(input('Masukkan tahun: '))

if pengecekan_tahun_kabisat(tahun):
    print(f'{tahun} adalah tahun kabisat')
else:
    print(f'{tahun} bukan tahun kabisat')