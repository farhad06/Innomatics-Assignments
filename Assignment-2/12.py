n=int(input())
s1=set(map(int,input().split()))
m=int(input())
s2=set(map(int,input().split()))  
s3=s1.union(s2)
count=0
for i in s3:
    count+=1
print(count) 