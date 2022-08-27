sample = float(input())
mean = float(input())
sdev = float(input())
interval = float(input())
m = float (input())

result = sdev / (sample**0.5)
print(round(mean - result*m,2))
print(round(mean + result*m,2))