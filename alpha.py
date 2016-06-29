from uncertainties import ufloat

N = ufloat(1341204, 4493)
B_1 = ufloat(0.001027, 0.000031)
B_2 = ufloat(0.05961, 0.00033)
B_3 = ufloat(0.01094, 0.00032)
e = ufloat(0.00857, 0.00001)
f = ufloat(0.40, 0.08) # pdg
e_m = ufloat(0.0000012, 0.0000004)
k = B_3/(f)
N_k = N*k
N_m = ufloat(7, 1)
print('Korrekturfaktor für N, k={}'.format(k))
print('Korrigiertes N={}'.format(N_k))
a = B_1*B_2*e/(N_k*e_m)
print('Das so bestimmte alpha, a={}'.format(a))
B_absch = N_m*a
print('OBERE AUSSCHLUSSGRENZE, B={}'.format(B_absch))
s_1 = ufloat(1.14e-6, 0.16e-6)
s_2 = ufloat(44.46e-6, 3.24e-6)
R = s_1/s_2
print('Korrekturfaktor für N, R={}'.format(R))
N_k = N*R
print('Korrigiertes N={}'.format(N_k))
a_2 = e*B_2*B_1/(N_k*e_m)
print('Das über die sigmas bestimmte alpha, a={}'.format(a_2))
B_absch = N_m*a_2
print('OBERE AUSSCHLUSSGRENZE, B={}'.format(B_absch))
