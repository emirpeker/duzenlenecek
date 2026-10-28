x = float(input("x koordinatini giriniz: "))
y = float(input("y koordinatini giriniz: "))
m = float(input("Doğrunun eğimini giriniz: "))
n = float(input("Doğrunun y eksenini kestiği noktayi giriniz: "))

if y == m * x + n:
    print("Nokta doğrunun üzerindedir.")
else:
    print("Nokta doğrunun üzerinde değildir.")
