def print_rangoli(size):
    # your code goes here
    Str = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        abs_i = abs(i)
        if abs_i >= 0:
            print_line = Str[size:abs_i:-1]+Str[abs_i:size]
            print ("--"*abs_i+ '-'.join(print_line)+"--"*abs_i)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)