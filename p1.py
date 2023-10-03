umur = 19
nama = shelom
print("halo, nama saya", nama, "umur saya", umur, "tahun")
print(f"halo, nama saya (nama) umur saya (umur) tahun")

x = 5
if x > 2:
   print(x)
   print(type(x))

x = "hello word"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ["aku", "kamu", "dia"]
print(type(x))

x = ("aku", "kamu", "dia")
print(type(x))

x = range(6)
print(type(x))

x = {"nama" : "shelom", "umur" : "19"}
print(type(x))

x = 20
y = 3
print(x, y)
print(float(x), float(y))

x = 20.3
y = 3.8
print(x, y)
print(int(x), int(y))

x = float("20.3")
y = int("3")
print(x, y)
print(int(x), float(y))

x = 3
if x > 2:
    x = x + 3
    if x > 5:
        x = x - 1
        print(x)

x = 3
if x > 3:
    x = x + 2
elif x > 5:
    x = x - 1
    print(x)

x = 5
if type(x) == int:
    x = x * 2
    if x > 5:
        x = x - 4
        print(x)
