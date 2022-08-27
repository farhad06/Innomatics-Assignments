import math
mean, std = 70, 10
value = lambda x: 0.5 * (1 + math.erf((x - mean) / (std * (2 ** 0.5))))


print(round((1-value(80))*100,2))
print(round((1-value(60))*100,2))
print(round((value(60))*100,2))