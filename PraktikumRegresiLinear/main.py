x = [10, 28, 29, 35, 48, 55, 71, 73, 80, 88, 91, 111, 131, 144, 160]
y = [29, 47, 55, 65, 79, 82, 92, 95, 100, 102, 110, 124, 127, 130, 152]
xy = [x * y for x, y in zip(x, y)]
kuadx = [x * y for x, y in zip(x, x)]
sigmaxy = sum(xy)
sigmax = sum(x)
sigmay = sum(y)
sigmakuadx = sum(kuadx)
a = (sigmay*sigmakuadx-sigmax*sigmaxy)/(15*sigmakuadx-sigmax*sigmax)
b = (15*sigmaxy-sigmax*sigmay)/(15*sigmakuadx-sigmax*sigmax)
angkaselanjutnya = int(input("Masukkan biaya promosi : "))
perkiraan = a+b*angkaselanjutnya
print("perkiraan penjualan rumah adalah : ", perkiraan)
