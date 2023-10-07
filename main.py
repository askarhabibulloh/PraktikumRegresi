import matplotlib.pyplot as plt
from scipy import stats
# x adalah uang untuk promosi dan y adalah hasil penjualan
x = [10, 28, 29, 35, 48, 55, 71, 73, 80, 88, 91, 111, 131, 144, 160]
y = [29, 47, 55, 65, 79, 82, 92, 95, 100, 102, 110, 124, 127, 130, 152]

slope, intercept, r, p, std_err = stats.linregress(x, y)

print('\n\n\n', 'slope = ', slope)
print('r = ', r)
print('intercept = ', intercept, "\n\n\n")


def myfunct(x):
    return intercept + slope * x


# mencari perkiraan penjualan berdasar jumlah uang promosi
p = int(input('Masukkan biaya promosi : '))
print('perkiraan rumah terjual : ', myfunct(p))


# show mapping

# mymodel = list(map(myfunct, x))

# plt.scatter(x, y)
# plt.plot(x, mymodel)
# plt.show()
