# print("Hello")
# print("saya sedang belajar python")

# a = 10 
# b = 3
# print("nilai variable a = ", a)
# print("nilai variable b = ", b)
# print("hasil jumlah a+b = ", a + b)

a = input("Masukan nilai a = ")
b = input("Masukan nilai b = ")
print("Nilai Variable a = ", a)
print("Nilai Variable b = ", b)

a = int(a)
b = int(b)
print("Hasil penjumlahan {1}+{0}=%d".format(a,b) %(a+b))
print("Hasil pembagian {1}/{0}=%d".format(a,b) %(a/b))