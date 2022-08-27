m=int(input())
s1=set(map(int,input().split()))
n=int(input())
s2=set(map(int,input().split()))
s3=s1.difference(s2)
c=0
for i in s3:
    c+=1
print(c)    