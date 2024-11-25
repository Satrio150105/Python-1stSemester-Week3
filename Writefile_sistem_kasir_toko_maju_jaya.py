print ("Selamat datang di Toko Maju Jaya")
print ("Senin, 4 September 2023       13.05")
print(" ")

print("DAFTAR BELANJA:")
item1 = 'Sabun'
item2 = 'Shampo'
item3 = 'Mie instant'
item4 = 'Detergen'
harga1 = 10000
harga2 = 15000
harga3 = 5000
harga4 = 17500

total = harga1 + harga2 + harga3 + harga4

print(item1, '        = Rp '+ str(harga1))
print(item2, '       = Rp '+ str(harga2))
print(item3, '  = Rp '+ str(harga3))
print(item4, '     = Rp '+ str(harga4))

print(" ")
print("Total = Rp "+ str(total))

with open ("Kuitansi.txt", "w") as writefile:
        writefile.write("Selamat Datang di Toko Maju Jaya\n")
        writefile.write(" \n")
        writefile.write("Kuitansi - 4 Septermber 2023\n")
        writefile.write(" \n")
        writefile.write(f'{item1} = Rp {harga1}\n')
        writefile.write(f'{item2} = Rp {harga2}\n')
        writefile.write(f'{item3} = Rp {harga3}\n')
        writefile.write(f'{item4} = Rp {harga4}\n')
        writefile.write(" \n")
        writefile.write("Total Belanja ="+ str(total))