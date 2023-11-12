class Karyawan:
    def __init__(self, nama):
        self.nama = nama
        self.gaji_pokok = 4000000
        self.uang_makan = 30000

    def hitung_gaji(self, hari_kerja):
        return self.gaji_pokok + self.uang_makan * hari_kerja


class Manager(Karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.tunjangan_profesi = 1500000
        self.uang_transport = 30000

    def hitung_gaji(self, hari_kerja):
        gaji_pokok = super().hitung_gaji(hari_kerja)
        return gaji_pokok + self.tunjangan_profesi + self.uang_transport * hari_kerja


class Admin(Karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.uang_transport = 15000
        self.uang_lembur_per_jam = 40000

    def hitung_gaji(self, hari_kerja, jam_lembur):
        gaji_pokok = super().hitung_gaji(hari_kerja)
        uang_lembur = self.uang_lembur_per_jam * jam_lembur
        return gaji_pokok + self.uang_transport * hari_kerja + uang_lembur


class Marketing(Karyawan):
    def __init__(self, nama):
        super().__init__(nama)
        self.uang_transport = 50000

    def hitung_gaji(self, hari_kerja):
        gaji_pokok = super().hitung_gaji(hari_kerja)
        return gaji_pokok + self.uang_transport * hari_kerja


def main():
    manager = Manager("Shelom Manager")
    admin = Admin("April Admin")
    marketing = Marketing("Myta Marketing")

    hari_kerja = 20
    jam_lembur_admin = 5

    gaji_manager = manager.hitung_gaji(hari_kerja)
    gaji_admin = admin.hitung_gaji(hari_kerja, jam_lembur_admin)
    gaji_marketing = marketing.hitung_gaji(hari_kerja)

    print(f"---------------**------------------")
    print(f"Gaji {manager.nama}   : Rp {gaji_manager}")
    print(f"Gaji {admin.nama}      : Rp {gaji_admin}")
    print(f"Gaji {marketing.nama}   : Rp {gaji_marketing}")
    print(f"---------------**------------------")

if __name__ == "__main__":
    main()