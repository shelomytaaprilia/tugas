class Orang():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFirstName(self):
        return self.firstName

    def getLastName(self):
        return self.lastName

class Alamat():
    def __init__(self, jalan, kota):
        self.jalan = jalan
        self.kota = kota

class Mahasiswa(Orang, Alamat):
        def __init__(self, firstName, lastName, nim, jalan, kota):
          self.nim = nim

          Orang.__init__(self, firstName, lastName)
          Alamat.__init__(self, jalan, kota)

        def __str__(self):
          return f"{self.firstName} {self.lastName} {self.nim}"

        def printData(self):
            print(f"Nama: {self.getFirstName()} {self.lastName}")
            print(f"NIM: {self.nim}")
            print(f"Alamat: {self.jalan}, {self.kota}")

mhs = Mahasiswa("Shelomyta", "Aprilia", "2207021", "Cibatu", "Garut")
mhs.printData()