# Enter your code here. Read input from STDIN. Print output to STDOUT
S = input()
k = input()
import re
p = re.compile(k)
res = p.search(S)
if not res: print ("(-1, -1)")
while res:
    print ("({0}, {1})".format(res.start(), res.end() - 1))
    res = p.search(S,res.start() + 1)