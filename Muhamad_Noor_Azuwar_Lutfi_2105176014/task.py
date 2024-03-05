class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def info(self):
        print("")
        print("Nama:", self.nama)
        print("Kelas:", self.kelas)
        print("Prodi:", self.prodi)
        print("Fakultas:", self.fakultas)
        print("Tempat Tinggal:", self.tempat_tinggal)
        print("Asal:", self.asal)

# Input data dari pengguna
nama = input("Masukkan nama: ")
kelas = input("Masukkan kelas: ")
prodi = input("Masukkan prodi: ")
fakultas = input("Masukkan fakultas: ")
tempat_tinggal = input("Masukkan tempat tinggal: ")
asal = input("Masukkan asal: ")

# Membuat objek Mahasiswa
mahasiswa1 = Mahasiswa(nama, kelas, prodi, fakultas, tempat_tinggal, asal)

# Menampilkan informasi mahasiswa
mahasiswa1.info()
