n = int(input())

for i in range(n):
    a = input()
    s1 = set(input().split())
    b = input()
    s2=set(input().split())
    print(s1.issubset(s2))