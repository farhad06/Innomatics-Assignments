# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string= re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(string.group(1) if string else -1)