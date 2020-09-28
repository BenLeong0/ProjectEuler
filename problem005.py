# LCM from 1 to l
# hcf * lcm = ab
from problem3 import all_factors

x = 2
lim = 27


def lcm(m, n):
    m_primes = all_factors(m)
    n_primes = all_factors(n)
    length = max(n_primes[-1], m_primes[-1]) + 1
    low_com_mult = 1
    for i in range(length):
        lcm_power = max(m_primes.count(i), n_primes.count(i))
        low_com_mult *= i ** lcm_power
    return low_com_mult


for j in range(2, lim + 1):
    x = lcm(x, j)

print(x)

check = True
for k in range(20):
    if x % (k+1) is False:
        check = False

print(check)
