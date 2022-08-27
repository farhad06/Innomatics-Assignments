# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
def isvalid(s):
    number=re.compile("[789]\d{9}$")
    return number.match(s)
n=int(input())
for i in range(n):
    if isvalid(input()):
        print("YES")
    else:
        print("NO")     
    
