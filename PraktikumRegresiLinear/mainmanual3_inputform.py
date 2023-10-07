n = int(input("Masukkan jumlah variabel : "))
x = []
y = []
for i in range(int(n)):
    # Mengambil input dan mengonversi ke integer
    elemen = int(input("Masukkan variabel independen ke-" + str(i+1) + ": "))
    x.append(elemen)  # Menambahkan elemen ke dalam list x


for i in range(int(n)):
    # Mengambil input dan mengonversi ke integer
    elemen = int(input("Masukkan variabel dependen ke-" + str(i+1) + ": "))
    y.append(elemen)  # Menambahkan elemen ke dalam list x


xy = [x * y for x, y in zip(x, y)]
kuadx = [x * y for x, y in zip(x, x)]
sigmaxy = sum(xy)
sigmax = sum(x)
sigmay = sum(y)
sigmakuadx = sum(kuadx)
a = (sigmay*sigmakuadx-sigmax*sigmaxy)/(n*sigmakuadx-sigmax*sigmax)
b = (n*sigmaxy-sigmax*sigmay)/(n*sigmakuadx-sigmax*sigmax)
angkaselanjutnya = int(
    input("Masukkan variabel independen yang akan dilihat perkiraannya : "))
perkiraan = a+b*angkaselanjutnya
print("perkiraan variabel dependen adalah : ", perkiraan)
