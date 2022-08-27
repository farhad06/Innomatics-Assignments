# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    user_id= ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', user_id)
        assert re.search(r'\d\d\d', user_id)
        assert not re.search(r'[^a-zA-Z0-9]', user_id)
        assert not re.search(r'(.)\1', user_id)
        assert len(user_id) == 10
    except:
        print('Invalid')
    else:
        print('Valid')