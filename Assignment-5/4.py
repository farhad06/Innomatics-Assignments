# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
string = '[qwrtypsdfghjklzxcvbnm]'
m = re.findall('(?<=' + string +')([aeiou]{2,})' + string, input(), re.I)
print('\n'.join(m or ['-1']))