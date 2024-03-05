Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Mahasiswa:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def info(self):
        print("Azuwar:", self.nama)
        print("A:", self.kelas)
        print("Pendidikan Komputer:", self.prodi)
        print("FKIP:", self.fakultas)
        print("Samarinda:", self.tempat_tinggal)
        print("Samarinda:", self.asal)

