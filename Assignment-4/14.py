def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        sub_str=''
        for s in string[i:i+k]:
            if s not in sub_str:
                sub_str+=s
        print(sub_str)    

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)