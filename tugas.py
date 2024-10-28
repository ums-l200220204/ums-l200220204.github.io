class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.spp_dibayar = False
        self.krs_diisi = False
        self.nilai_akhir = None

    def bayar_spp(self):
        print(f"{self.nama} sedang membayar SPP...")
        self.spp_dibayar = True
        print("SPP berhasil dibayar.\n")

    def isi_krs(self):
        if self.spp_dibayar:
            print(f"{self.nama} sedang mengisi KRS...")
            self.krs_diisi = True
            print("KRS berhasil diisi.\n")
        else:
            print("SPP belum dibayar! Isi KRS tidak bisa dilakukan.\n")

    def ikut_perkuliahan(self):
        if self.krs_diisi:
            print(f"{self.nama} sedang mengikuti perkuliahan...\n")
        else:
            print("KRS belum diisi! Tidak bisa mengikuti perkuliahan.\n")

    def ikut_ujian(self):
        if self.krs_diisi:
            print(f"{self.nama} sedang mengikuti ujian...\n")
        else:
            print("KRS belum diisi! Tidak bisa mengikuti ujian.\n")

    def terima_nilai_akhir(self, nilai):
        if self.krs_diisi:
            print(f"{self.nama} menerima nilai akhir: {nilai}\n")
            self.nilai_akhir = nilai
        else:
            print("KRS belum diisi! Tidak bisa menerima nilai.\n")

# Simulasi Proses Kuliah
mahasiswa = Mahasiswa("Budi", "12345678")

# 1. Bayar SPP
mahasiswa.bayar_spp()

# 2. Isi KRS
mahasiswa.isi_krs()

# 3. Ikut Perkuliahan
mahasiswa.ikut_perkuliahan()

# 4. Ikut Ujian
mahasiswa.ikut_ujian()

# 5. Terima Nilai Akhir
mahasiswa.terima_nilai_akhir(85)
