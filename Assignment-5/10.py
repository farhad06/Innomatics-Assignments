# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
color_code=r'(#[0-9a-fA-F]{3,6}){1,2}[^\n ]'
for _ in range(int(input())):
    for i in re.findall(color_code,input()):
        print(i)