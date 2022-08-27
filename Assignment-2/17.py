k=int(input())
room=input().split()
s1=set()
s2=set()
for i in room:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)
captain_room=list(s3)
print(int(captain_room[0])) 