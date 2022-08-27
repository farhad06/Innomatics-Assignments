from math import erf
maxi = float(input())
n = int(input())
m = float(input())
std = float(input())
mean = n*m
stand = std*(n**0.5)
result = lambda x : 0.5*(1+erf((x-mean)/(stand*(2**0.5))))
p = result(maxi)
p = round(p, 4)
print(p)