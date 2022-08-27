a, b = input().split()

arr =input().split()

s1 = set(input().split())
s2= set(input().split())
print (sum([(i in s1) - (i in s2) for i in arr]))