class Program:
    def __init__(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def tampil_data(self):
        print("Nama: ", self.nama)
        print("Kelas: ", self.kelas)
        print("Prodi: ", self.prodi)
        print("Fakultas: ", self.fakultas)
        print("Tempat Tinggal: ", self.tempat_tinggal)
        print("Asal: ", self.asal)

program1 = Program("Rifki", "A", "Pendidikan Komputer", "Keguruan dan Ilmu Pendidikan", "Jalan. Cendana Gang 2 Rt. 17 No. 56", "Samarinda")
program1.tampil_data()
