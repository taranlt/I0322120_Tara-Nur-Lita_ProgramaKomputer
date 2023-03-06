#program string menggantikan nama pada undangan

tulisan1= "kepada yth: "
tulisan2= "nama yang diundang: tara "
tulisan3= "alamat kota Jakarta "

print("===============")
#kop surat pertama
print(tulisan1)
print(tulisan2)
print(tulisan3)
print("===============")
#kop surat kedua
print(tulisan1)
print(tulisan2.replace("tara","dela"))
print(tulisan3.replace("Jakarta","Tangerang"))
print("===============")
#kop surat ketiga
print(tulisan1)
print(tulisan2.replace("tara","ara"))
print(tulisan3.replace("Jakarta","Batam"))
print("===============")