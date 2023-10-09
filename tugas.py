class Mahasiswa:
    def __init__(self, nama, nim, umur):
        self.nama = nama
        self.nim = nim
        self.umur = umur

    def __str__(self):
        return f"Nama saya adalah {self.nama}, dan NIM saya adalah {self.nim}"
    
    def tahunlahir(self):
        return 2023 - self.umur
    
    def akt(self):
        return f"{self.nama}, mahasiswa angkatan 20{self.nim[:2]}"

saya = Mahasiswa("Shelomyta", "2207021", 19)
print("Tahun lahir saya adalah", saya.tahunlahir())
print("Saya", saya.akt())