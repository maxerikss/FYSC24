import numpy as np
from uncertainties import ufloat

Vus = ufloat(0.2243, 0.0008)
Vud = ufloat(0.97373, 0.00073)
Vcs = ufloat(0.975, 0.006)
Vcd = ufloat(0.221, 0.004)

a_calc = Vus**2 / Vud**2
a_meas = ufloat(0.1033, 0.0013)
print('a')
print(a_calc)
print(a_calc/a_meas * 100)

b_calc = Vcd**2 / Vcs**2
b_meas = ufloat(0.0368, 0.0005)
print('b')
print(b_calc)
print(b_calc/b_meas * 100)

c_calc = (Vcd**2 * Vus**2) / (Vcs**2 * Vud**2)
c_meas = ufloat(0.00379, 0.00018)
print('c')
print(c_calc)
print(c_calc/c_meas * 100)