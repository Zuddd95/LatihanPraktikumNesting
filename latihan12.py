# import datetime

# # 1. Multi-keys: tuple (nim, kode_mk) sebagai satu kunci
# nilai_ujian = {
#     ("26050001", "TI101"): 85,
#     ("26050001", "TI102"): 90,
#     ("26050002", "TI101"): 78,
# }
# print(nilai_ujian[("26050001", "TI102")])
# print(("26050002", "TI101") in nilai_ujian)

# # 2. Dictionary data mahasiswa
# mhs_rani = {
#     'nama': 'Rani Putri',
#     'nim': '26050001',
#     'sks_lulus': 20,
#     'beasiswa': False,
#     'lahir': datetime.datetime(2007, 4, 10)  # tahun, bulan, tanggal
# }
# mhs_bima = {
#     'nama': 'Bima Pratama',
#     'nim': '26050002',
#     'sks_lulus': 24,
#     'beasiswa': True,
#     'lahir': datetime.datetime(2007, 10, 21)
# }
# mhs_citra = {
#     'nama': 'Citra Lestari',
#     'nim': '26050003',
#     'sks_lulus': 22,
#     'beasiswa': True,
#     'lahir': datetime.datetime(2006, 12, 5)
# }

# # 3. Nesting: dictionary berisi dictionary
# daftar_mhs = {
#     'MHS001': mhs_rani,
#     'MHS002': mhs_bima,
#     'MHS003': mhs_citra,
# }

# # 4. Menampilkan data dalam bentuk tabel
# print(f"{'KODE':<7} {'Nama':<14} {'SKS':<4} {'Beasiswa':<9} {'Lahir':<10}")
# print("-" * 50)

# for kode in daftar_mhs:
#     nama = daftar_mhs[kode]['nama']
#     sks = daftar_mhs[kode]['sks_lulus']
#     beasiswa = daftar_mhs[kode]['beasiswa']
#     lahir = daftar_mhs[kode]['lahir'].strftime("%d-%m-%Y")
#     print(f"{kode:<7} {nama:<14} {sks:<4} {str(beasiswa):<9} {lahir:<10}")

# print(daftar_mhs['MHS002']['nama'])

# import datetime

# template_mhs = {
#     'nama': 'nama',
#     'nim': '00000000',
#     'sks_lulus': 0,
#     'lahir': datetime.datetime(1111, 1, 11)
# }

# print(f"{'SELAMAT DATANG':^20}")
# print(f"{'DATA MAHASISWA':^20}")
# print("-" * 20)

# mhs_baru = dict.fromkeys(template_mhs.keys())
# print(mhs_baru)

# mhs_baru['nama'] = input("Nama Mahasiswa: ")
# mhs_baru['nim'] = input("NIM Mahasiswa: ")
# mhs_baru['sks_lulus'] = int(input("SKS Lulus: "))

# tahun = int(input("Tahun lahir (YYYY): "))
# bulan = int(input("Bulan lahir (1-12): "))
# tanggal = int(input("Tanggal lahir (1-31): "))
# mhs_baru['lahir'] = datetime.datetime(tahun, bulan, tanggal)

# print(mhs_baru)

import datetime
import os
import string
import random

template_mhs = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': datetime.datetime(1111, 1, 11)
}

data_mhs = {}

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-" * 20)

    mhs_baru = dict.fromkeys(template_mhs.keys())
    mhs_baru['nama'] = input("Nama Mahasiswa: ")
    mhs_baru['nim'] = input("NIM Mahasiswa: ")
    mhs_baru['sks_lulus'] = int(input("SKS Lulus: "))

    tahun = int(input("Tahun lahir (YYYY): "))
    bulan = int(input("Bulan lahir (1-12): "))
    tanggal = int(input("Tanggal lahir (1-31): "))
    mhs_baru['lahir'] = datetime.datetime(tahun, bulan, tanggal)

    # membuat kunci acak 6 huruf kapital
    kunci = ''.join(random.choice(string.ascii_uppercase) for i in range(6))
    data_mhs.update({kunci: mhs_baru})

    print(f"\n{'KUNCI':<7} {'Nama':<14} {'NIM':<10} {'SKS':<5} {'Tanggal Lahir':<13}")
    print("-" * 52)

    for kode in data_mhs:
        nama = data_mhs[kode]['nama']
        nim = data_mhs[kode]['nim']
        sks = data_mhs[kode]['sks_lulus']
        lahir = data_mhs[kode]['lahir'].strftime("%d-%m-%Y")
        print(f"{kode:<7} {nama:<14} {nim:<10} {sks:<5} {lahir:<13}")

    lanjut = input("\nMau tambah lagi (y/n)? ")
    if lanjut == "n":
        break

print("\nAkhir dari program, terima kasih")