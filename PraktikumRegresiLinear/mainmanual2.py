x = [1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700]
y = [245, 312, 279, 308, 199, 219, 405, 324, 319, 255]
n = len(x)
xy = [x * y for x, y in zip(x, y)]
kuadx = [x * y for x, y in zip(x, x)]
sigmaxy = sum(xy)
sigmax = sum(x)
sigmay = sum(y)
sigmakuadx = sum(kuadx)
a = (sigmay*sigmakuadx-sigmax*sigmaxy)/(n*sigmakuadx-sigmax*sigmax)
b = (n*sigmaxy-sigmax*sigmay)/(n*sigmakuadx-sigmax*sigmax)
angkaselanjutnya = int(input("Masukkan luas rumah : "))
perkiraan = a+b*angkaselanjutnya
print("perkiraan harga rumah adalah : ", perkiraan)
