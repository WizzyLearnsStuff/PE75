import numpy as np
from math import gcd

N = 1500000
T = np.zeros(N + 1)

for m in range(1, 1225, 2):
    for n in range(1, min(((N - m * m) // (m)) + 1, m), 2):
        if gcd(m, n) != 1: continue
        abc = m * (m + n)

        T[abc] += 1
        if abc == 120:
            print(m, n, m * m - n * n, 2 * m * n, m * m + n * n)

        for k in range(2, N // abc + 1):
            T[abc * k] += 1

print(np.sum(T == 1))
print(T[120] == 3, T[12] == 1, T[24] == 1, T[30] == 1, T[36] == 1, T[40] == 1, T[48] == 1)