s1 = set(map(str, input().split(' ')))
superset = []
for i in range(int(input())):
    superset.append(s1.issuperset(set(map(str, input().split(' ')))))
print(all(superset))