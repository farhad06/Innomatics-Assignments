import math

a = int(input())
b = int(input())
m = int(input())
sig = int(input())

m_sum = b * m 
sig_sum = math.sqrt(b) * sig

def central(a, m, sig):
    Z = (a - m)/sig
    return 0.5*(1 + math.erf(Z/(math.sqrt(2))))

print(round(central(a, m_sum, sig_sum), 4))